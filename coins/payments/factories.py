import factory
import faker
import operator

from accounts.factories import AccountFactory
from payments.choices import DIRECTION
from payments.models import Payment

fake = faker.Factory.create('en_US')


class PaymentFactory(factory.django.DjangoModelFactory):
    account = factory.SubFactory(AccountFactory)
    related_account = factory.SubFactory(AccountFactory)
    amount = factory.LazyAttribute(lambda _: fake.pydecimal(
        left_digits=4, right_digits=2, positive=True
    ))
    direction = factory.Iterator(DIRECTION, getter=operator.itemgetter(0))

    class Meta:
        model = Payment
