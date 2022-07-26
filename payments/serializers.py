from countryinfo import CountryInfo
from django.db.models import Case, When, Value, IntegerField
from django.db.models.functions import Upper

from svfoundation.utils import get_country_currencies
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
    currencies = serializers.SerializerMethodField()

    def get_currencies(self, obj):
        request = self.context['request']
        country_code = request.session.get('country_code')
        country_currencies = []
        if country_code:
            country_currencies = get_country_currencies(country_code)
        currencies = obj.currencies.annotate(
            name_upper=Upper('name')
        ).annotate(custom_order=Case(
            When(name__in=country_currencies, then=Value(0)),
            default=Value(1),
            output_field=IntegerField(),
        )).order_by('custom_order', 'order')
        return PaymentSystemCurrencySerializer(currencies, many=True).data

    class Meta:
        model = PaymentSystem
        fields = ('name', 'currencies')
