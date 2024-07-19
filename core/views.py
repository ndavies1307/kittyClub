from django.shortcuts import render
from .models import Cat

# Create your views here.

def index(request):
    cat_videos = Cat.objects.all()
    featured_vid = cat_videos.last() if cat_videos.last() is not None else None

    context = {
        'cat_videos': cat_videos,
        'featured_vid': featured_vid
    }

    return render(request, 'index.html', context)

def Shane(request):
    shane_videos = Cat.objects.filter(tag='Shane')
    shane_feature = shane_videos.last() if shane_videos.count() > 0 else None

    context = {
        'shane_videos': shane_videos,
        'shane_feature': shane_feature,
    }

    return render(request, 'Shane.html', context)

def Reggie(request):
    reggie_videos = Cat.objects.filter(tag='Reggie')
    reggie_feature = reggie_videos.last() if reggie_videos.count() > 0 else None

    context = {
        'reggie_videos': reggie_videos,
        'reggie_feature': reggie_feature,
    }
    return render(request, 'Reggie.html', context)