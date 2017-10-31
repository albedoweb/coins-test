"""coins URL Configuration"""

from django.conf.urls import include, url
from django.contrib import admin

from accounts import urls as accounts_urls
from payments import urls as payments_urls


urlpatterns = [
    url(r'^v1/accounts', include(accounts_urls)),
    url(r'^v1/payments', include(payments_urls)),
    url(r'^admin/', admin.site.urls),
]
