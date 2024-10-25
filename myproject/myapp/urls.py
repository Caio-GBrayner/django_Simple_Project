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

from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'episodes', views.EpisodeViewSet)
router.register(r'playlists', views.PlaylistViewSet)
router.register(r'jobpostings', views.JobPostingViewSet)
router.register(r'ecosystemmaps', views.EcosystemMapViewSet)
router.register(r'transcriptions', views.TranscriptionViewSet)
router.register(r'glossaryterms', views.GlossaryTermViewSet)
router.register(r'quizzes', views.QuizViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

