<<<<<<< HEAD
=======

>>>>>>> ad36b6214467c0d387e2d33aa9d24c693721e329
from rest_framework import serializers
from .models import Episode, Playlist, JobPosting, EcosystemMap, Transcription, GlossaryTerm, Quiz

class EpisodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Episode
        fields = '__all__'

class PlaylistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playlist
        fields = '__all__'

class JobPostingSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobPosting
        fields = '__all__'

class EcosystemMapSerializer(serializers.ModelSerializer):
    class Meta:
        model = EcosystemMap
        fields = '__all__'

class TranscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transcription
        fields = '__all__'

class GlossaryTermSerializer(serializers.ModelSerializer):
    class Meta:
        model = GlossaryTerm
        fields = '__all__'

class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = '__all__'