from modeltranslation.translator import register, TranslationOptions
from .models import News, NewsTag


@register(News)
class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'annotation', 'content')


@register(NewsTag)
class NewsTagTranslationOptions(TranslationOptions):
    fields = ('name',)
