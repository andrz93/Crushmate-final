from django.urls import path
from . import views

urlpatterns = [
    path('like/<int:user_id>/', views.like_user, name='like_user'),
]
