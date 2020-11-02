from django.urls import path
from . import views
#현재 디렉토리 내에 views.py를 불러오므로 from 에는 현재 디렉토리를 의미하는 . 을 써줌.

urlpatterns = [
    path('create/', views.create),
    path('new/', views.new),
    path('index/', views.index),
    path('<int:post_id>/', views.detail),
    path('<int:post_id>/delete/', views.delete),
    path('<int:post_id>/edit/', views.edit),
    path('<int:post_id>/update/', views.update),
]