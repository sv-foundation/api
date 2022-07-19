from django.db import models
from django_extensions.db.models import TimeStampedModel
from currencies import Currency


CURRENCIES_CHOICES = [(code, code) for code in Currency.money_formats.keys()]  # [(UAH, UAH), (USD, USD), ...]


class PaymentDetails(TimeStampedModel):
    currency_code = models.CharField(max_length=5, choices=CURRENCIES_CHOICES, default='UAH', primary_key=True)
    address = models.CharField(max_length=255, null=True)
    card_number = models.CharField(max_length=20, null=True, blank=True)
    iban = models.CharField('IBAN', max_length=40)
    bic = models.CharField('BIC', max_length=20, null=True, blank=True)
    fund_name = models.CharField(max_length=255, null=True, blank=True)
    bank = models.CharField(max_length=255, null=True, blank=True)
    corespondent_banks = models.TextField(null=True, blank=True)
    payment_purpose = models.CharField(max_length=255, null=True, blank=True)
    is_visible = models.BooleanField(null=False, default=True, help_text='Is visible on website')

    class Meta:
        verbose_name_plural = 'payment details'

    def __str__(self):
        return self.currency_code


class FundDocument(TimeStampedModel):
    name = models.CharField(max_length=255, null=False)
    file = models.FileField(upload_to='fond_documents/')

    def __str__(self):
        return self.name
