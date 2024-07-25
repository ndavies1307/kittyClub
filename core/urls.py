from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.contrib import admin
from core import views

urlpatterns = [
    path('', views.index, name='index'),
    path('Shane/', views.shane, name='Shane'),
    path('Reggie/', views.reggie, name='Reggie'),
    path('', views.index, name='Home'),
    path('videos/<str:pk>/', views.details, name='details'),
    path('search/', views.search, name='search'),
    path('about/', views.about, name='about'),

]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)