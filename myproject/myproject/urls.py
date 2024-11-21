"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from rest_framework import routers
from django.contrib.auth import views as auth_views
from myapp import views 

router = routers.DefaultRouter()
router.register(r'episodes', views.EpisodeViewSet)
router.register(r'playlists', views.PlaylistViewSet)
router.register(r'jobpostings', views.JobPostingViewSet)
router.register(r'ecosystemmaps', views.EcosystemMapViewSet)
router.register(r'transcriptions', views.TranscriptionViewSet)
router.register(r'glossaryterms', views.GlossaryTermViewSet)
router.register(r'quizzes', views.QuizViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', include('myapp.urls')),  # Inclua as URLs do seu aplicativo
    path('api/login/', views.LoginView.as_view(), name='login-api'),
]

