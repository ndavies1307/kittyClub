from django.shortcuts import render, redirect
from .models import Cat
import uuid

# Create your views here.

def index(request):
    cat_videos = Cat.objects.all()
    featured_vid = cat_videos.last() if cat_videos.last() is not None else None

    context = {
        'cat_videos': cat_videos,
        'featured_vid': featured_vid
    }

    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')

def shane(request):
    shane_videos = Cat.objects.filter(tags='Shane')
    shane_feature = shane_videos.last() if shane_videos.count() > 0 else None

    context = {
        'shane_videos': shane_videos,
        'shane_feature': shane_feature,
    }

    return render(request, 'Shane.html', context)

def reggie(request):
    reggie_videos = Cat.objects.filter(tags='Reggie')
    reggie_feature = reggie_videos.last() if reggie_videos.count() > 0 else None

    context = {
        'reggie_videos': reggie_videos,
        'reggie_feature': reggie_feature,
    }
    return render(request, 'Reggie.html', context)

def details(request, pk):
    # Assuming pk represents a tag

    cat_videos = Cat.objects.filter(tags=pk)

    context = {
        'video_tags': pk,
        'cat_videos': cat_videos
    }

    return render(request, 'videos.html', context)


def search(request):
    if request.method == 'POST':
        search_term = request.POST['search_term']
        cat_videos = Cat.objects.filter(tags__icontains=search_term)

        context = {
            'cat_videos': cat_videos,
            'search_term': search_term,
        }
        return render(request, 'search.html', context)
    else:
        return redirect('/')
