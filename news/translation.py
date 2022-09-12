from modeltranslation.translator import register, TranslationOptions
from .models import News, NewsTag


@register(News)
class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'annotation', 'content')
    required_languages = ('uk', 'en')


@register(NewsTag)
class NewsTagTranslationOptions(TranslationOptions):
    fields = ('name',)
    required_languages = ('uk', 'en')
