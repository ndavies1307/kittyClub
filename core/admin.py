from django.contrib import admin
from .models import Cat

# Register your models here.
def index(request):
    return admin

class CatAdmin(admin.ModelAdmin):
    list_display = ('title', 'tags')

admin.site.register(Cat, CatAdmin)
