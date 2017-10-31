from __future__ import unicode_literals

from model_utils import Choices


DIRECTION = Choices(
    ('1', 'incoming', 'Incoming'),
    ('2', 'outgoing', 'Outgoing'),
)
