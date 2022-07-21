from svfoundation import settings
from .models import News, NewsTag
from rest_framework import serializers
from urllib.parse import urljoin


class NewsTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsTag
        fields = ['slug', 'name']


class NewsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ['slug', 'title', 'publication_date', 'annotation', 'preview_photo']


class NewsDetailsSerializer(serializers.ModelSerializer):
    tags = NewsTagSerializer(many=True)
    preview_photo = serializers.SerializerMethodField()
    content = serializers.SerializerMethodField()

    def get_preview_photo(self, obj):
        return urljoin(settings.API_URL, obj.preview_photo.url)

    def get_content(self, obj):
        # TODO make it more clear
        return obj.content.replace('/media/django-summernote', f'{settings.API_URL}/media/django-summernote')

    class Meta:
        model = News
        fields = ['slug', 'title', 'publication_date', 'annotation', 'preview_photo', 'content', 'tags']

