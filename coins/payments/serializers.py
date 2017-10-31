from rest_framework import serializers

from accounts.models import Account
from payments.models import Payment


class PaymentListSerializer(serializers.ModelSerializer):
    from_account = serializers.SlugRelatedField(
        read_only=True, slug_field='id', source='account'
    )
    to_account = serializers.SlugRelatedField(
        read_only=True, slug_field='id', source='related_account'
    )
    amount = serializers.DecimalField(
        coerce_to_string=False, decimal_places=2, max_digits=6
    )

    class Meta:
        model = Payment
        fields = (
            'id', 'from_account', 'to_account', 'amount', 'direction'
        )


class PaymentCreateSerializer(serializers.ModelSerializer):
    from_account = serializers.SlugRelatedField(
        queryset=Account.objects.all(), slug_field='id',
        source='account'
    )
    to_account = serializers.SlugRelatedField(
        queryset=Account.objects.all(), slug_field='id',
        source='related_account'
    )
    amount = serializers.DecimalField(
        coerce_to_string=False, decimal_places=2, max_digits=6
    )

    def validate(self, data):
        if data['account'] == data['related_account']:
            raise serializers.ValidationError(
                'Can\'t create payment to same account'
            )
        return data

    class Meta:
        model = Payment
        fields = (
            'from_account', 'to_account', 'amount'
        )
