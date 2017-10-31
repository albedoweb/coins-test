# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from accounts.choices import CURRENCY


class Account(models.Model):
    id = models.SlugField(primary_key=True, unique=True, max_length=50)
    owner = models.CharField(max_length=50)
    balance = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    currency = models.CharField(max_length=3, choices=CURRENCY)
