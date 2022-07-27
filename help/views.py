from copy import deepcopy

from django.core.mail import send_mail, EmailMessage
from django.http import Http404
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.views import APIView

from help.mail_templates.txt_template import HELP_TEMPLATE
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
        files_copy = deepcopy(files)
        data = deepcopy(request.data)
        if 'file' in data:
            del data['file']
        serializer = HelpRequestSerializer(data=data, context={'documents': files})
        if serializer.is_valid():
            serializer.save()
            try:
                msg = HELP_TEMPLATE.format(full_name=serializer.data['full_name'],
                                           organization_name=serializer.data['organization_name'],
                                           email=serializer.data['email'],
                                           phone_number=serializer.data['phone_number'],
                                           message=serializer.data['message'])
                mail = EmailMessage('Потребую допомоги - з форми на сторінці '
                                    'https://beta.svfoundation.org.ua/potrebuiu-dopomohy',
                                    msg,
                                    settings.EMAIL_HOST_USER,
                                    settings.HELP_EMAIL_RECIPIENTS)
                for file in files_copy:
                    mail.attach(file.name, file.read(), file.content_type)
                mail.send(fail_silently=False)
            except Exception as e:
                return Response(str(e), status=status.HTTP_400_BAD_REQUEST)
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)  # NOQA
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
