from django.conf.urls import url

from payments import views


urlpatterns = [
    url(r'',
        views.PaymentView.as_view(),
        name='payment'),
]
