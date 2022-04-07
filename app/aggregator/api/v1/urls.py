from django.contrib import admin
from django.urls import path, include

from aggregator.api.v1.views import LogListView

urlpatterns = [
    path('logs/', LogListView.as_view()),
]
