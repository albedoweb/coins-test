from django.db import models, transaction
from rest_framework.exceptions import ValidationError

from accounts.models import Account
from payments.choices import DIRECTION


class PaymentManager(models.Manager):
    @transaction.atomic
    def create_payment(self, from_account, to_account, amount):
        """
        Create transactions for money transfer between two accounts

        We use double entry bookkeeping here, so each payment will be
        represented as two records in DB table. One for outgoing and one
        for incoming transaction.
        """
        from_account = Account.objects.select_for_update().get(
            pk=from_account
        )
        to_account = Account.objects.select_for_update().get(
            pk=to_account
        )

        if from_account.balance < amount:
            raise ValidationError(
                'Insufficient funds on the balance for {0}'.format(
                    from_account.id
                )
            )

        self.create(
            account=from_account,
            related_account=to_account,
            amount=amount,
            direction=DIRECTION.outgoing
        )
        self.create(
            account=to_account,
            related_account=from_account,
            amount=amount,
            direction=DIRECTION.incoming
        )
        from_account.balance -= amount
        from_account.save(update_fields=['balance'])

        to_account.balance += amount
        to_account.save(update_fields=['balance'])
