from datetime import datetime, date

from django.db import models
from django_extensions.db.models import TimeStampedModel


class NewsTag(TimeStampedModel):
    slug = models.SlugField(max_length=255, unique=True)
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class News(TimeStampedModel):
    main_photo = models.ImageField(upload_to='main_photos/%Y-%m-%d/',
                                   help_text='Photo that displayed in top of news page',
                                   null=True, blank=False)
    preview_photo = models.ImageField(upload_to='previews/%Y-%m-%d/', help_text='Photo that displayed in news list')
    title = models.CharField(max_length=255, null=False)
    slug = models.SlugField(max_length=255, unique=True)
    publication_date = models.DateField(default=date.today)
    annotation = models.TextField(null=False)
    content = models.TextField(null=False)
    tags = models.ManyToManyField(NewsTag, related_name='news')

    class Meta:
        verbose_name_plural = 'News'

    def __str__(self):
        return self.title
