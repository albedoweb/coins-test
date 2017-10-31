# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.generics import ListCreateAPIView

from payments.models import Payment
from payments.serializers import (
    PaymentCreateSerializer,
    PaymentListSerializer,
)


class PaymentView(ListCreateAPIView):
    queryset = Payment.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return PaymentCreateSerializer
        return PaymentListSerializer

    def perform_create(self, serializer):
        """
        We overwrite default behavior of `perform_create` function
        to run custom fuction for payment creation

        :param serializer: payments.serializers.PaymentCreateSerializer
        :return: None
        """
        data = serializer.data
        Payment.objects.create_payment(
            data['from_account'],
            data['to_account'],
            data['amount']
        )
