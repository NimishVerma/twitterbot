# project_name/urls.py
from django.conf.urls import include, url, patterns
from django.contrib import admin

from slack_webhook import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^webhook', views.webhook, name='webhook'),
]