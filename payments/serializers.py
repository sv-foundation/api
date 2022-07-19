from .models import PaymentDetails, FundDocument
from rest_framework import serializers


class FundDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = FundDocument
        fields = ('name', 'file')


class CurrencyListSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentDetails
        fields = ('currency_code',)


class PaymentDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentDetails
        exclude = ('created', 'modified', 'is_visible')
