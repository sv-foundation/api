from django.contrib import admin
from .models import FundDocument, PaymentDetails
from modeltranslation.admin import TranslationAdmin


@admin.register(FundDocument)
class FundDocumentAdmin(TranslationAdmin):
    ...


@admin.register(PaymentDetails)
class PaymentDetailsAdmin(admin.ModelAdmin):
    ...
