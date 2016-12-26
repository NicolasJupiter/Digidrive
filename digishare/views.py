# from nicemovies.forms import VideoForm
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.shortcuts import render
from .forms import _videoForm
#from nicemovies.models import _video
# from django.urls import reverse_lazy


def landing(request):
    if request.method == "POST":
        form = _videoForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
    else:
        form = _videoForm()
    return render(request, 'index.html', {'form': form})

# def next(request):
#     content = ""
#     return render(request, 'base.html')
#
# def back(request):
#     return render(request, 'back.html')

# def front(request):
#     user1 = request.POST.get('Name', None)
#     video1 = request.POST.get('url', None)
#
#     _video1 = _video(video=video1,user=user1)
#     _video1.save()
#
#     return render(request, 'front.html')

