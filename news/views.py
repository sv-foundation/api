from django.http import Http404
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend, OrderingFilter
from rest_framework import mixins, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from news.models import News, NewsTag
from news.serializers import NewsListSerializer, NewsDetailsSerializer, NewsTagSerializer


class NewsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = News.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['tags__slug']
    ordering = ('-publication_date', 'id')

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
