import binascii
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.views import APIView

from help.mail_templates.txt_template import HELP_TEMPLATE
from help.models import HelpRequest
from help.serializers import HelpRequestSerializer
from help.tasks import send_help_email


class HelpRequestView(APIView):
    parser_classes = (MultiPartParser, FormParser,)

    def get(self, request):
        help_requests = HelpRequest.objects.all()
        serializer = HelpRequestSerializer(help_requests, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request, format=None):
        files = request.FILES.getlist('file', None)
        data = request.data
        if 'file' in data:
            del data['file']
        serializer = HelpRequestSerializer(data=data, context={'documents': files})
        if serializer.is_valid():
            files_data = []
            for file in files:
                files_data.append((file.name, (binascii.hexlify(file.read())).decode(), file.content_type))

            serializer.save()
            try:
                msg = HELP_TEMPLATE.format(full_name=serializer.data['full_name'],
                                           organization_name=serializer.data['organization_name'],
                                           email=serializer.data['email'],
                                           phone_number=serializer.data['phone_number'],
                                           message=serializer.data['message'])
                send_help_email.apply_async(kwargs={'message': msg, 'files_data': files_data})
            except Exception as e:
                return Response(str(e), status=status.HTTP_400_BAD_REQUEST)
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)  # NOQA
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
