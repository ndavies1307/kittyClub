from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def Shane(request):
    return render(request, 'Shane.html')

def Reggie(request):
    return render(request, 'Reggie.html')