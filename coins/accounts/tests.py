# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from django.urls import reverse

from accounts.factories import AccountFactory


class AccountTestCase(TestCase):
    def test_account_list(self):
        account = AccountFactory()
        account2 = AccountFactory()

        url = reverse('account-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)
        self.assertListEqual(
            [
                {
                    'id': account.id,
                    'owner': account.owner,
                    'balance': account.balance,
                    'currency': account.currency,
                },
                {
                    'id': account2.id,
                    'owner': account2.owner,
                    'balance': account2.balance,
                    'currency': account2.currency,
                },
            ],
            response.data
        )
