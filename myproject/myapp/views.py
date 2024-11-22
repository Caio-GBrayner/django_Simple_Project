from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm
from .models import Episode, Playlist, JobPosting, EcosystemMap, Transcription, GlossaryTerm, Quiz
from rest_framework import generics
from .serializers import (
    EpisodeSerializer, PlaylistSerializer, JobPostingSerializer,
    EcosystemMapSerializer, TranscriptionSerializer, GlossaryTermSerializer, QuizSerializer
)

# Views para renderização
def home(request):
    episodes = Episode.objects.all()
    context = {'episodes': episodes}
    return render(request, 'myapp/home.html', context)

def search(request):
    query = request.GET.get('q')
    results = []  # Substitua pela lógica para obter resultados da pesquisa
    return render(request, 'myapp/search_results.html', {'query': query, 'results': results})

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')  # Redirecione para a página inicial após o registro
    else:
        form = CustomUserCreationForm()
    return render(request, 'myapp/register.html', {'form': form})

@login_required
def admin_panel(request):
    return render(request, 'myapp/admin_panel.html')


# API Views
class EpisodeList(generics.ListCreateAPIView):
    queryset = Episode.objects.all()
    serializer_class = EpisodeSerializer

class EpisodeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Episode.objects.all()
    serializer_class = EpisodeSerializer

class PlaylistList(generics.ListCreateAPIView):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer

class PlaylistDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer

class JobPostingList(generics.ListCreateAPIView):
    queryset = JobPosting.objects.all()
    serializer_class = JobPostingSerializer

class JobPostingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = JobPosting.objects.all()
    serializer_class = JobPostingSerializer

class EcosystemMapList(generics.ListCreateAPIView):
    queryset = EcosystemMap.objects.all()
    serializer_class = EcosystemMapSerializer

class EcosystemMapDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = EcosystemMap.objects.all()
    serializer_class = EcosystemMapSerializer

class TranscriptionList(generics.ListCreateAPIView):
    queryset = Transcription.objects.all()
    serializer_class = TranscriptionSerializer

class TranscriptionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Transcription.objects.all()
    serializer_class = TranscriptionSerializer

class GlossaryTermList(generics.ListCreateAPIView):
    queryset = GlossaryTerm.objects.all()
    serializer_class = GlossaryTermSerializer

class GlossaryTermDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = GlossaryTerm.objects.all()
    serializer_class = GlossaryTermSerializer

class QuizList(generics.ListCreateAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer

class QuizDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
