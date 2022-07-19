from .models import News, NewsTag
from rest_framework import serializers


class NewsTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsTag
        fields = ['slug', 'name']


class NewsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ['slug', 'title', 'publication_date', 'annotation', 'preview_photo']


class NewsDetailsSerializer(NewsListSerializer):
    tags = NewsTagSerializer(many=True)

    class Meta:
        model = News
        fields = NewsListSerializer.Meta.fields + ['content', 'tags']
