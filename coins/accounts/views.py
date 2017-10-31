# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.generics import ListAPIView

from accounts.models import Account
from accounts.serializers import AccountSerializer


class AccountListView(ListAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
