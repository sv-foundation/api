from bs4 import BeautifulSoup

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
    main_photo = serializers.SerializerMethodField()
    content = serializers.SerializerMethodField()

    def get_main_photo(self, obj):
        return urljoin(settings.API_URL, (obj.main_photo or obj.preview_photo).url)

    def get_content(self, obj):
        content = obj.content
        soup = BeautifulSoup(content, "html.parser")
        for tag in soup():
            del tag['style']
        for img in soup.find_all('img'):
            rel_position = img['src'].find('media')
            rel_link = img['src'][rel_position:]
            img['src'] = urljoin(settings.API_URL, rel_link)
        return str(soup)

    class Meta:
        model = News
        fields = ['slug', 'title', 'publication_date', 'annotation', 'main_photo', 'content', 'tags']

