from .models import News, NewsTag
from rest_framework import serializers


class NewsTagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = NewsTag
        fields = ['name']


class NewsListSerializer(serializers.ModelSerializer):
    tags = NewsTagSerializer(many=True)

    class Meta:
        model = News
        fields = ['id', 'title', 'publication_date', 'annotation', 'preview_photo', 'tags']


class NewsDetailsSerializer(serializers.ModelSerializer):
    tags = NewsTagSerializer(many=True)

    class Meta:
        model = News
        fields = ['id', 'title', 'publication_date', 'content', 'preview_photo', 'tags']
