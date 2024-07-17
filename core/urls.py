from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('Shane/', views.Shane, name='Shane'),
    path('Reggie/', views.Reggie, name='Reggie'),
]
