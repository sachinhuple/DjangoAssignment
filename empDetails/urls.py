'''
Created on 30-Dec-2016

@author: sachin
'''
from django.conf.urls import url
from django.contrib import admin

from .views import (
    form_view,
    search_view,
    base_view,
    )

urlpatterns = [
    url(r'^$', base_view),
    url(r'^detailsform/', form_view),
    url(r'^searchform/', search_view),
]