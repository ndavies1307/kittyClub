from django.contrib import admin
from .models import Cat

# Register your models here.
def index(request):
    return admin

admin.site.register(Cat)
