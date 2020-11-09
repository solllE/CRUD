from django.urls import path
from . import views
#현재 디렉토리 내에 views.py를 불러오므로 from 에는 현재 디렉토리를 의미하는 . 을 써줌.

app_name = 'board'

urlpatterns = [
    path('create/', views.create, name='create'),
    path('new/', views.new, name='new'),
    path('index/', views.index, name='index'),
    path('<int:post_id>/', views.detail, name='detail'),
    path('<int:post_id>/delete/', views.delete, name='delete'),
    path('<int:post_id>/edit/', views.edit, name='edit'),
    path('<int:post_id>/update/', views.update, name='update'),
    path('<int:post_id>/comments/create/', views.comments_create, name='comments_create'),
    path('<int:post_id>/comments/<int:comment_id>/delete/', views.comments_delete, name='comments_delete'),
]