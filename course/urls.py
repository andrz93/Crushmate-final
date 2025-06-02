from django.urls import path
from . import views

urlpatterns = [
    path('', views.course_schedule_view, name='course'),  # 課表首頁
    path('suggestions/', views.course_suggestions, name='course_suggestions'),  # 🔥 課名推薦 API
]
