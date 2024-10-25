from django.contrib import admin
from .models import Episode, Playlist, JobPosting, EcosystemMap, Transcription, GlossaryTerm, Quiz

admin.site.register(Episode)
admin.site.register(Playlist)
admin.site.register(JobPosting)
admin.site.register(EcosystemMap)
admin.site.register(Transcription)
admin.site.register(GlossaryTerm)
admin.site.register(Quiz)
