from django.urls import path

from .views import LogListView, LogCreate

urlpatterns = [
    path('logs/', LogListView.as_view()),
    path('logs/create/', LogCreate.as_view()),
]
