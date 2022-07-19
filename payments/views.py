import json
from decimal import Decimal, InvalidOperation

from cloudipsp import Checkout
from rest_framework.response import Response
from rest_framework import viewsets, mixins, views, status

from svfoundation import settings
from .models import FundDocument, PaymentDetails, CURRENCIES_CHOICES
from .serializers import FundDocumentSerializer, PaymentDetailsSerializer


class FundDocumentsSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = FundDocument.objects.all()
    serializer_class = FundDocumentSerializer


class PaymentDetailsSet(viewsets.ReadOnlyModelViewSet):
    queryset = PaymentDetails.objects.filter(is_visible=True).all()
    serializer_class = PaymentDetailsSerializer


class MakePayment(views.APIView):
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
        if currency not in [currency[0] for currency in CURRENCIES_CHOICES]:
            errors['currency'] = ['Invalid currency']
        coins = None
        try:
            coins = int(Decimal(amount) * 100)
            assert coins > 0
        except (InvalidOperation, ValueError, AssertionError):
            errors['amount'] = ['Invalid amount']
        return {'currency': currency, 'amount': coins}, errors

