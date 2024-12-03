from django.contrib import admin
from django.urls import path, include
from myapp.views import CustomLoginView, CustomSignupView

urlpatterns = [
    path('admin/', admin.site.urls),  # Rota para o admin
    path('login/', CustomLoginView.as_view(), name='account_login'),  # Usando a view personalizada para login
    path('signup/', CustomSignupView.as_view(), name='account_signup'),  # Usando a view personalizada para cadastro
    path('accounts/', include('allauth.urls')),  # Incluindo todas as URLs do Allauth
    path('', include('myapp.urls')),  # Incluindo URLs do aplicativo principal (myapp)
]
