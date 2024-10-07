from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Episode
from .forms import EpisodeForm

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