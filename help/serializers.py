from .models import HelpRequest, Document
from rest_framework import serializers


class DocumentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Document
        fields = ['file']


class HelpRequestSerializer(serializers.ModelSerializer):
    documents = DocumentSerializer(many=True, read_only=True)

    def create(self, validated_data):
        documents = self.context['documents']
        help_request = HelpRequest.objects.create(**validated_data)
        for document in documents:
            Document.objects.create(help_request=help_request,
                                    name=document.name,
                                    file=document)
        return help_request

    class Meta:
        model = HelpRequest
        fields = '__all__'
