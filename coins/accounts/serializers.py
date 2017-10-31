from rest_framework import serializers

from accounts.models import Account


class AccountSerializer(serializers.ModelSerializer):
    balance = serializers.DecimalField(
        coerce_to_string=False, decimal_places=2, max_digits=6
    )

    class Meta:
        model = Account
        fields = (
            'id', 'owner', 'balance', 'currency'
        )
