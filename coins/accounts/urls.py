from django.conf.urls import url

from accounts import views


urlpatterns = [
    url(r'',
        views.AccountListView.as_view(),
        name='account-list'),
]
