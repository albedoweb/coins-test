# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from accounts.models import Account
from payments.choices import DIRECTION
from payments.managers import PaymentManager


class Payment(models.Model):
    account = models.ForeignKey(
        Account, null=False, blank=False, on_delete=models.CASCADE,
        related_name='payments'
    )
    related_account = models.ForeignKey(
        Account, null=False, blank=False, on_delete=models.CASCADE,
        related_name='related_payments'
    )
    amount = models.DecimalField(
        max_digits=6, decimal_places=2
    )
    direction = models.CharField(max_length=1, choices=DIRECTION)

    objects = PaymentManager()
