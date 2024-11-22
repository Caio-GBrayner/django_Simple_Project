from django.urls import path
from . import views, api_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='myapp/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='myapp/logout.html'), name='logout'),
    path('admin_panel/', views.admin_panel, name='admin_panel'),

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
