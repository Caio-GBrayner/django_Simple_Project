from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Episode
from .forms import EpisodeForm
from rest_framework import viewsets
from .models import Episode, Playlist, JobPosting, EcosystemMap, Transcription, GlossaryTerm, Quiz
from .serializers import (EpisodeSerializer, PlaylistSerializer, JobPostingSerializer, 
EcosystemMapSerializer, TranscriptionSerializer, GlossaryTermSerializer, QuizSerializer)



@login_required
def episode_list(request):
    episodes = Episode.objects.all()
    return render(request, 'myapp/episode_list.html', {'episodes': episodes})

@login_required
def episode_create(request):
    if request.method == 'POST':
        form = EpisodeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('episode_list')
    else:
        form = EpisodeForm()
    return render(request, 'myapp/episode_form.html', {'form': form})

@login_required
def episode_update(request, pk):
    episode = get_object_or_404(Episode, pk=pk)
    if request.method == 'POST':
        form = EpisodeForm(request.POST, request.FILES, instance=episode)
        if form.is_valid():
            form.save()
            return redirect('episode_list')
    else:
        form = EpisodeForm(instance=episode)
    return render(request, 'myapp/episode_form.html', {'form': form})

@login_required
def episode_delete(request, pk):
    episode = get_object_or_404(Episode, pk=pk)
    if request.method == 'POST':
        episode.delete()
        return redirect('episode_list')
    return render(request, 'myapp/episode_confirm_delete.html', {'episode': episode})





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
