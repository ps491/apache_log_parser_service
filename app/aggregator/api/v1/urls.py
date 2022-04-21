from django.urls import path

from .views import LogListView

urlpatterns = [
    path('logs/', LogListView.as_view()),
]
