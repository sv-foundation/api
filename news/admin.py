from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import News, NewsTag
from modeltranslation.admin import TranslationAdmin


@admin.register(NewsTag)
class NewsTagAdmin(TranslationAdmin):
    prepopulated_fields = {'slug': ('name',)}


@admin.register(News)
class NewsAdmin(TranslationAdmin, SummernoteModelAdmin):
    summernote_fields = ('content',)
    prepopulated_fields = {'slug': ('title',)}
