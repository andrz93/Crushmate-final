from django.urls import path, include
from . import views


urlpatterns = [
    path("", views.homepage, name="home"),
    path("chat/", include('chat.urls'), name="chat"),       #new
    path("settings/", include('settingsapp.urls'), name="settings"),        #new
    path("profilepage/", include('profilepage.urls'), name="profilepage"),
]
