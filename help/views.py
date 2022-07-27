from copy import deepcopy

from django.core.mail import send_mail
from django.http import Http404
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.views import APIView

from help.models import HelpRequest
from help.serializers import HelpRequestSerializer
from svfoundation import settings
import asyncio


class HelpRequestView(APIView):
    parser_classes = (MultiPartParser, FormParser,)

    def get(self, request):
        help_requests = HelpRequest.objects.all()
        serializer = HelpRequestSerializer(help_requests, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request, format=None):
        files = request.FILES.getlist('file', None)
        data = deepcopy(request.data)
        if 'file' in data:
            del data['file']
        serializer = HelpRequestSerializer(data=data, context={'documents': files})
        if serializer.is_valid():
            serializer.save()
            send_mail(subject='Help request',
                      message='Test',
                      from_email=settings.EMAIL_HOST_USER,
                      recipient_list=['sashayak2203@gmail.com'])
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)  # NOQA
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
