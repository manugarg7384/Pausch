from django.conf.urls import patterns, include, url
from django.contrib import admin

from pauschproject import views

urlpatterns = patterns('',
    url(r'^$', views.home),
    url(r'^change-panel$', views.panel_input),
)
