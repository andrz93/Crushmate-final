# match/urls.py
from django.urls import path
from .views import swipe

app_name = 'match'

urlpatterns = [
    path('swipe/', swipe, name='swipe'),
]
