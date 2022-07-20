from django.db import models
from django_extensions.db.models import TimeStampedModel
from currencies import Currency

CURRENCIES_CHOICES = [(code, code) for code in Currency.money_formats.keys()]  # [(UAH, UAH), (USD, USD), ...]


class PaymentDetails(TimeStampedModel):
    currency_code = models.CharField(max_length=10, primary_key=True)
    is_visible = models.BooleanField(null=False, default=True, help_text='Is visible on website')

    class Meta:
        verbose_name_plural = 'payment details'

    def __str__(self):
        return self.currency_code


class PaymentDetailsField(TimeStampedModel):
    name = models.CharField(max_length=255, null=True, blank=True)
    value = models.CharField(max_length=255)
    payment_details = models.ForeignKey(PaymentDetails, on_delete=models.CASCADE, related_name='fields')

    def __str__(self):
        return self.name or self.value


class PaymentSystemCurrency(models.Model):
    name = models.CharField(max_length=10, primary_key=True)

    def __str__(self):
        return self.name


class PaymentSystem(TimeStampedModel):
    NAMES = (
        ('FONDY', 'Fondy'),
    )
    name = models.CharField(max_length=255, choices=NAMES, default='FONDY', primary_key=True)
    is_visible = models.BooleanField(null=False, default=True, help_text='Is visible on website')
    currencies = models.ManyToManyField(PaymentSystemCurrency)

    def __str__(self):
        return self.name


class FundDocument(TimeStampedModel):
    name = models.CharField(max_length=255, null=False)
    file = models.FileField(upload_to='fond_documents/')

    def __str__(self):
        return self.name
