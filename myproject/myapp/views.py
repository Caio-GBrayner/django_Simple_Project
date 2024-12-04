from django.shortcuts import render, get_object_or_404, redirect
from .models import Episode, Playlist, JobPosting, EcosystemMap, Transcription, GlossaryTerm, Quiz
from .forms import EpisodeForm, CustomSignupForm, CustomSigninForm
from rest_framework import viewsets
from django.urls import reverse_lazy
from .serializers import (
    EpisodeSerializer, PlaylistSerializer, JobPostingSerializer, 
    EcosystemMapSerializer, TranscriptionSerializer, GlossaryTermSerializer, QuizSerializer
)
from allauth.account.views import LoginView, SignupView

# Criando uma view personalizada para login
class CustomLoginView(LoginView):
    form_class = CustomSigninForm  # Especificando o formulário personalizado
    template_name = 'account/login.html'  # Especificando o template personalizado

    def form_valid(self, form):
        # Aqui você pode adicionar lógica personalizada antes de chamar o método pai
        response = super().form_valid(form)
        # Adicione qualquer lógica adicional necessária
        return response

# Criando uma view personalizada para cadastro
class CustomSignupView(SignupView):
    form_class = CustomSignupForm  # Especificando o formulário personalizado
    template_name = 'account/cadastro.html'

    def form_valid(self, form):
        print("Formulário é válido. Dados:", form.cleaned_data)  # Adicione este log
        response = super().form_valid(form)
        # Adicione qualquer lógica adicional necessária aqui
        return redirect(reverse_lazy('account_login')) # Redirecionando para a página de login após o cadastro

# Defina outras views conforme necessário
def index(request):
    return render(request, 'myapp/index.html')


def sobre(request):
    return render(request, 'myapp/sobre.html')

def explore(request):
    return render(request, 'myapp/explore.html')

# Viewsets para a API
class EpisodeViewSet(viewsets.ModelViewSet):
    queryset = Episode.objects.all()
    serializer_class = EpisodeSerializer

class PlaylistViewSet(viewsets.ModelViewSet):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer

class JobPostingViewSet(viewsets.ModelViewSet):
    queryset = JobPosting.objects.all()
    serializer_class = JobPostingSerializer

class EcosystemMapViewSet(viewsets.ModelViewSet):
    queryset = EcosystemMap.objects.all()
    serializer_class = EcosystemMapSerializer

class TranscriptionViewSet(viewsets.ModelViewSet):
    queryset = Transcription.objects.all()
    serializer_class = TranscriptionSerializer

class GlossaryTermViewSet(viewsets.ModelViewSet):
    queryset = GlossaryTerm.objects.all()
    serializer_class = GlossaryTermSerializer

class QuizViewSet(viewsets.ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    
from django.shortcuts import render
from .forms import SearchForm

def search(request):
    form = SearchForm()
    results = []
    if request.method == 'GET':
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            results = Episode.objects.filter(title__icontains=query)
    return render(request, 'search_results.html', {'form': form, 'results': results})
