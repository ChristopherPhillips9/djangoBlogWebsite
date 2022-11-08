#!/usr/bin/env python
__author__ = "Christopher Phillips, christopher.phillips9@snhu.edu"

from django.urls import path
from .views import BligListViews

urlpatterns = [
    path('', BlogListView.as_view(), name='home')
]

