"""crud_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from crud_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main),

    # crud_app에 사용되는 url은 board로 따로 묶어 관리
    # 모든 앱의 url을 여기 작성하는 것은 비효율적이기 때문
    path('board/', include('crud_app.app_urls')),
]
