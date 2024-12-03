from django.urls import path, include
from rest_framework import routers
from . import views

# Configurando o router para as rotas da API
router = routers.DefaultRouter()
router.register(r'episodes', views.EpisodeViewSet)
router.register(r'playlists', views.PlaylistViewSet)
router.register(r'jobpostings', views.JobPostingViewSet)
router.register(r'ecosystemmaps', views.EcosystemMapViewSet)
router.register(r'transcriptions', views.TranscriptionViewSet)
router.register(r'glossaryterms', views.GlossaryTermViewSet)
router.register(r'quizzes', views.QuizViewSet)

web_urlpatterns = [
    path('search/', views.search, name='search'),
    path('', views.index, name='index'),  # Página inicial do aplicativo
    path('sobre/', views.sobre, name='sobre'),  # Página sobre
    path('explore/', views.explore, name='explore'),  # Página explorar
    path('cadastro/', views.CustomSignupView.as_view(), name='account_signup'), # Página de cadastro personalizada
    path('login/', views.CustomLoginView.as_view(), name='account_login'),  # Página de login personalizada
]

api_urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

urlpatterns = web_urlpatterns + api_urlpatterns
