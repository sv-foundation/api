from .models import PaymentDetails, FundDocument, PaymentDetailsField, PaymentSystem, PaymentSystemCurrency
from rest_framework import serializers


class FundDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = FundDocument
        fields = ('name', 'file')


class PaymentDetailsFieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentDetailsField
        fields = ('name', 'value')


class PaymentDetailsSerializer(serializers.ModelSerializer):
    fields = PaymentDetailsFieldSerializer(many=True)

    class Meta:
        model = PaymentDetails
        fields = ('currency_code', 'fields')


class PaymentSystemCurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentSystemCurrency
        fields = ('name',)


class PaymentSystemListSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentSystem
        fields = ('name',)


class PaymentSystemSerializer(serializers.ModelSerializer):
    currencies = PaymentSystemCurrencySerializer(many=True)

    class Meta:
        model = PaymentSystem
        fields = ('name', 'currencies')
