from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='myapp/login.html'), name='login'),
    path('', views.episode_list, name='episode_list'),  
    path('episodes/', views.episode_list, name='episode_list'),
    path('episodes/new/', views.episode_create, name='episode_create'),
    path('episodes/<int:pk>/edit/', views.episode_update, name='episode_update'),
    path('episodes/<int:pk>/delete/', views.episode_delete, name='episode_delete'),
]
