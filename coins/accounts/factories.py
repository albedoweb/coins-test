import string

import factory
import faker
import operator
from factory import fuzzy

from accounts.choices import CURRENCY
from accounts.models import Account


fake = faker.Factory.create('en_US')


class AccountFactory(factory.django.DjangoModelFactory):
    id = fuzzy.FuzzyText(length=10, chars=string.ascii_lowercase)
    owner = fuzzy.FuzzyText(length=10)
    balance = factory.LazyAttribute(lambda _: fake.pydecimal(
        left_digits=4, right_digits=2, positive=True
    ))
    currency = factory.Iterator(CURRENCY, getter=operator.itemgetter(0))

    class Meta:
        model = Account
