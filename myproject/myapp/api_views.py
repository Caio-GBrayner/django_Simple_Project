from rest_framework import generics
from .models import Episode, Playlist, JobPosting, EcosystemMap, Transcription, GlossaryTerm, Quiz
from .serializers import (
    EpisodeSerializer, PlaylistSerializer, JobPostingSerializer,
    EcosystemMapSerializer, TranscriptionSerializer, GlossaryTermSerializer, QuizSerializer
)

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
