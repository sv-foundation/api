from django.contrib import admin
from .models import FundDocument, PaymentDetails, PaymentDetailsField, PaymentSystemCurrency, PaymentSystem
from modeltranslation.admin import TranslationAdmin


@admin.register(FundDocument)
class FundDocumentAdmin(TranslationAdmin):
    ...


class PaymentDetailsFieldInline(admin.TabularInline):
    model = PaymentDetailsField


@admin.register(PaymentDetails)
class PaymentDetailsAdmin(admin.ModelAdmin):
    inlines = [PaymentDetailsFieldInline]


@admin.register(PaymentSystemCurrency)
class PaymentSystemCurrencyAdmin(admin.ModelAdmin):
    ...


class PaymentSystemCurrencyInline(admin.TabularInline):
    model = PaymentSystem.currencies.through


@admin.register(PaymentSystem)
class PaymentSystemAdmin(admin.ModelAdmin):
    inlines = [PaymentSystemCurrencyInline]
    exclude = ('currencies',)
