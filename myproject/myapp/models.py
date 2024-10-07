from django.db import models

class Episode(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    audio_file = models.FileField(upload_to='episodes/')
    publication_date = models.DateField()

    def __str__(self):
        return self.title

class Playlist(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    episodes = models.ManyToManyField(Episode)

    def __str__(self):
        return self.name

class JobPosting(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    company = models.CharField(max_length=100)
    date_posted = models.DateField()

    def __str__(self):
        return self.title

class EcosystemMap(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Transcription(models.Model):
    episode = models.ForeignKey(Episode, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return f'Transcription for {self.episode.title}'

class GlossaryTerm(models.Model):
    term = models.CharField(max_length=100)
    definition = models.TextField()

    def __str__(self):
        return self.term

class Quiz(models.Model):
    question = models.CharField(max_length=200)
    answer = models.CharField(max_length=200)
    episode = models.ForeignKey(Episode, on_delete=models.CASCADE)

    def __str__(self):
        return self.question
