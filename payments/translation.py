from modeltranslation.translator import register, TranslationOptions
from .models import FundDocument


@register(FundDocument)
class FundDocumentTranslationOptions(TranslationOptions):
    fields = ('name', 'file')
    required_languages = ('uk', 'en')
