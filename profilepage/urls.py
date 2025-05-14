from django.urls import path
from .views import profile_page, delete_photo

urlpatterns = [
    path('profile/', profile_page, name='profilepage'),
    path('delete/<int:photo_id>/', delete_photo, name='delete_photo'),
]
