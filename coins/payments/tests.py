# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from django.urls import reverse

from accounts.factories import AccountFactory
from payments.choices import DIRECTION
from payments.factories import PaymentFactory
from payments.models import Payment


class PaymentTestCase(TestCase):
    def test_payment_list(self):
        payment = PaymentFactory()
        payment2 = PaymentFactory()

        url = reverse('payment')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)

        self.assertListEqual(
            [
                {
                    'id': payment.id,
                    'from_account': payment.account.pk,
                    'to_account': payment.related_account.pk,
                    'amount': payment.amount,
                    'direction': payment.direction,
                },
                {
                    'id': payment2.id,
                    'from_account': payment2.account.pk,
                    'to_account': payment2.related_account.pk,
                    'amount': payment2.amount,
                    'direction': payment2.direction,
                },
            ],
            response.data
        )

    def test_create_payment(self):
        account = AccountFactory(balance=150)
        account2 = AccountFactory(balance=0)

        url = reverse('payment')
        response = self.client.post(
            url,
            data={
                'from_account': account.id,
                'to_account': account2.id,
                'amount': 100,
            },
            format='json',
        )

        payment = Payment.objects.filter(
            account__pk=account.id,
            related_account__pk=account2.id,
        ).first()

        self.assertEqual(response.status_code, 201)
        self.assertIsNotNone(payment)
        self.assertEqual(payment.amount, 100)
        self.assertEqual(payment.direction, DIRECTION.outgoing)

        payment2 = Payment.objects.filter(
            account__pk=account2.id,
            related_account__pk=account.id,
        ).first()
        self.assertIsNotNone(payment2)
        self.assertEqual(payment2.amount, 100)
        self.assertEqual(payment2.direction, DIRECTION.incoming)

        account.refresh_from_db()
        self.assertEqual(account.balance, 50)

        account2.refresh_from_db()
        self.assertEqual(account2.balance, 100)

    def test_bad_balance(self):
        account = AccountFactory(balance=50)
        account2 = AccountFactory()

        url = reverse('payment')
        response = self.client.post(
            url,
            data={
                'from_account': account.id,
                'to_account': account2.id,
                'amount': 100,
            },
            format='json',
        )

        self.assertEqual(response.status_code, 400)

    def test_same_account(self):
        account = AccountFactory(balance=50)

        url = reverse('payment')
        response = self.client.post(
            url,
            data={
                'from_account': account.id,
                'to_account': account.id,
                'amount': 100,
            },
            format='json',
        )

        self.assertEqual(response.status_code, 400)

    def test_bad_account(self):
        account = AccountFactory(balance=500)

        url = reverse('payment')
        response = self.client.post(
            url,
            data={
                'from_account': account.id,
                'to_account': 'bad_account',
                'amount': 100,
            },
            format='json',
        )
        self.assertEqual(response.status_code, 400)
