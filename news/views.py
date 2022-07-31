from django.http import Http404
from django.shortcuts import get_object_or_404
from django.utils.text import slugify
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins, viewsets, filters
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from news.models import News, NewsTag
from news.serializers import NewsListSerializer, NewsDetailsSerializer, NewsTagSerializer


class NewsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = News.objects.all()
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    ordering = ('-publication_date', 'id')
    filterset_fields = ['tags__slug']

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return NewsDetailsSerializer
        return NewsListSerializer

    def retrieve(self, request, *args, **kwargs):
        slug = kwargs.get('slug')
        news = get_object_or_404(self.queryset, slug=slug)
        serializer = NewsDetailsSerializer(news)
        return Response(serializer.data)


class NewsTagsList(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = NewsTag.objects.all()
    serializer_class = NewsTagSerializer


@api_view(['GET'])
def health(request):
    return Response('OK', status=200)


def get_date_from_str(date_str):
    MONTHS = ['Січня', 'Лютого', 'Березня', 'Квітня', 'Травня', 'Червня', 'Липня']
    from datetime import datetime
    date_str = date_str.replace(',', '')
    d, m, y = date_str.split()
    m = MONTHS.index(m) + 1
    return datetime.strptime(f'{d} {m} {y}', '%d %m %Y').date()


def parse_news_page(url):
    from bs4 import BeautifulSoup
    import urllib.request
    import io
    import requests
    from django_summernote.models import Attachment
    from django.core.files.images import ImageFile

    with urllib.request.urlopen(url) as f:
        content = f.read().decode('utf-8')
    soup = BeautifulSoup(content, features='html.parser')
    _, article, *_ = soup.find_all('article')
    content = article.find('div', {'class': 'entry-content'})
    for gallery in content.find_all('div', {'class': 'gallery'}):
        new_gallery = soup.new_tag('div')
        new_gallery['class'] = 'gallery'
        for a in gallery.find_all('a'):
            img_tag = a.find('img')
            srcset = img_tag.get('srcset').split(', ')
            for src in srcset:
                link, *_ = src.split(' ')
                if 'x' not in link[-15:]:
                    break
            new_img = soup.new_tag('img')
            *_, image_name = link.split('/')
            image_bytes = requests.get(link).content
            image = ImageFile(io.BytesIO(image_bytes), name=image_name)
            attachment = Attachment.objects.create(name=image_name, file=image)
            print(f'attachement({link})', attachment)
            new_img['src'] = attachment.file.url
            new_item = soup.new_tag('div')
            new_item['class'] = 'galleryItem'
            new_item.append(new_img)
            new_gallery.append(new_item)
        gallery.replace_with(new_gallery)
    return str(content)


@api_view(['GET'])
def parse(request):
    from bs4 import BeautifulSoup
    import urllib.request
    import requests
    import io
    from django.core.files.images import ImageFile
    from unidecode import unidecode

    for page in range(1, 4):
        print('page', page)
        with urllib.request.urlopen(f'https://svfoundation.org.ua/novyny/page/{page}/') as f:
            list_content = f.read().decode('utf-8')

        soup = BeautifulSoup(list_content, features='html.parser')
        articles = soup.find_all('article')
        for article in articles:
            print('--------------------------------------------------------------')
            preview_image = article.find('img')
            preview_src = preview_image.get('src')
            preview_file = requests.get(preview_src).content
            print(preview_src)
            header = article.find('h4')
            print(header.text)
            annotation = header.find_next('div')
            print(annotation.text)
            link = annotation.find_next('a')
            print(link.get('href'))
            pub_date = get_date_from_str(link.text.strip())
            print(pub_date)
            *_, image_name = preview_src.split('/')
            image = ImageFile(io.BytesIO(preview_file), name=image_name)
            content = parse_news_page(link.get('href'))
            print(content)

            News.objects.create(
                title_uk=header.text,
                annotation_uk=annotation.text,
                preview_photo=image,
                main_photo=image,
                content_uk=content,
                publication_date=pub_date,
                slug=slugify(unidecode(header.text))
            )

        print(len(articles))
    return Response('OK', status=200)
