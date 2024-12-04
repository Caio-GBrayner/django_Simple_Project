<<<<<<< HEAD
from django.urls import path, include
from rest_framework import routers
from . import views
from .views import CustomSignupView

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
    path('sobre/', views.sobre, name='about_us'),  # Página sobre
    path('explore/', views.explore, name='explore'),  # Página explorar
    path('cadastro/', CustomSignupView.as_view(), name='account_signup'),
    path('login/', views.CustomLoginView.as_view(), name='account_login'),  # Página de login personalizada
]

api_urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

urlpatterns = web_urlpatterns + api_urlpatterns
=======
from django.urls import path
from . import views, api_views  # Certifique-se de importar views e api_views corretamente
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='myapp/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='myapp/logout.html'), name='logout'),
    path('admin_panel/', views.admin_panel, name='admin_panel'),

    # API URLs
    path('api/episodes/', api_views.EpisodeList.as_view(), name='episode_list_api'),
    path('api/episodes/<int:pk>/', api_views.EpisodeDetail.as_view(), name='episode_detail_api'),
    path('api/playlists/', api_views.PlaylistList.as_view(), name='playlist_list_api'),
    path('api/playlists/<int:pk>/', api_views.PlaylistDetail.as_view(), name='playlist_detail_api'),
    path('api/jobpostings/', api_views.JobPostingList.as_view(), name='jobposting_list_api'),
    path('api/jobpostings/<int:pk>/', api_views.JobPostingDetail.as_view(), name='jobposting_detail_api'),
    path('api/ecosystemmaps/', api_views.EcosystemMapList.as_view(), name='ecosystemmap_list_api'),
    path('api/ecosystemmaps/<int:pk>/', api_views.EcosystemMapDetail.as_view(), name='ecosystemmap_detail_api'),
    path('api/transcriptions/', api_views.TranscriptionList.as_view(), name='transcription_list_api'),
    path('api/transcriptions/<int:pk>/', api_views.TranscriptionDetail.as_view(), name='transcription_detail_api'),
    path('api/glossaryterms/', api_views.GlossaryTermList.as_view(), name='glossaryterm_list_api'),
    path('api/glossaryterms/<int:pk>/', api_views.GlossaryTermDetail.as_view(), name='glossaryterm_detail_api'),
    path('api/quizzes/', api_views.QuizList.as_view(), name='quiz_list_api'),
    path('api/quizzes/<int:pk>/', api_views.QuizDetail.as_view(), name='quiz_detail_api'),
]
>>>>>>> ad36b6214467c0d387e2d33aa9d24c693721e329
