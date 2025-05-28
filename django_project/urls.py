"""
URL configuration for django_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView, RedirectView  # 之後用來做首頁
from navigation import views as nav_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', RedirectView.as_view(url='/accounts/login/', permanent=False)),    #一runserver就會跳轉到login頁面
    path("admin/", admin.site.urls),
    path('accounts/', include('allauth.urls')),  # allauth 登入/註冊/登出
    # 這邊是Andrew後來加的頁面跳轉的連結
    path('', include('navigation.urls')),  # 預設首頁交給 navigation
    path('home/', nav_views.homepage, name='home'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
