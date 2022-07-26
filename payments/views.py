import json
from decimal import Decimal, InvalidOperation

from cloudipsp import Checkout
from countryinfo import CountryInfo
from django.db.models import Case, When, Value, IntegerField
from django.db.models.functions import Upper
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets, mixins, views, status

from svfoundation import settings
from svfoundation.utils import get_country_by_ip, get_country_currencies
from .models import FundDocument, PaymentDetails, PaymentSystem
from .serializers import (
    FundDocumentSerializer, PaymentDetailsSerializer, PaymentSystemListSerializer,
    PaymentSystemSerializer
)


class FundDocumentsSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = FundDocument.objects.all()
    serializer_class = FundDocumentSerializer


class PaymentDetailsSet(viewsets.ReadOnlyModelViewSet):
    queryset = PaymentDetails.objects.filter(is_visible=True).all()
    serializer_class = PaymentDetailsSerializer

    def get_queryset(self):
        country_code = self.request.session.get('country_code')
        country_currencies = []
        if country_code:
            country_currencies = get_country_currencies(country_code)
        return PaymentDetails.objects.filter(is_visible=True).annotate(
            currency_code_upper=Upper('currency_code')
        ).annotate(custom_order=Case(
            When(currency_code_upper__in=country_currencies, then=Value(0)),
            default=Value(1),
            output_field=IntegerField(),
        )).order_by('custom_order', 'order', '-created')


class PaymentSystemsSet(viewsets.ReadOnlyModelViewSet):
    queryset = PaymentSystem.objects.filter(is_visible=True)

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return PaymentSystemSerializer
        return PaymentSystemListSerializer


class MakeFondyPayment(views.APIView):
    def post(self, request, format=None):
        checkout = Checkout(api=settings.fondy_api)
        data = request.data
        validated_data, errors = self.validate(data)
        if errors:
            return Response(errors, status=status.HTTP_400_BAD_REQUEST)
        res = checkout.url(validated_data)
        url = res.get('checkout_url')
        return Response({'checkout_url': url})

    def validate(self, data) -> (dict, dict):
        currency = data.get('currency')
        amount = data.get('amount')
        errors = {}
        fondy_system = PaymentSystem.objects.get(name='FONDY')
        if not fondy_system:
            errors['error'] = ['Payment system not exists']
            return {}, errors
        allowed_currencies = [currency.name for currency in fondy_system.currencies.all()]
        if currency not in allowed_currencies:
            errors['currency'] = ['Invalid currency']
        coins = None
        try:
            coins = int(Decimal(amount) * 100)
            assert coins > 0
        except (InvalidOperation, ValueError, AssertionError):
            errors['amount'] = ['Invalid amount']
        return {'currency': currency, 'amount': coins}, errors


@api_view(['GET'])
def check_country(request):
    ip = request.META.get('REMOTE_ADDR', None)
    if not ip:
        return Response("Coudn't get REMOTE_ADDR", status=400)
    country_code = get_country_by_ip(ip)
    if country_code:
        request.session['country_code'] = country_code
        supported_languages = [lang[0] for lang in settings.LANGUAGES]
        country_languages = CountryInfo(country_code).languages()
        suitable_languages = list(set(supported_languages).intersection(set(country_languages)))
        if suitable_languages:
            language = suitable_languages[0]
        elif country_code.lower() == 'ua':
            language = 'uk'
        else:
            language = 'en'
    else:
        return Response("Coudn't get country from IP", status=400)
    return Response({'country': country_code, 'language': language}, status=200)
