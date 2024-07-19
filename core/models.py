from django.contrib.auth.models import User
from django.db import models
import uuid
from django.conf import settings

# Create your models here.

class Cat(models.Model):

    CAT_TAGS = [
        ('shane', 'Shane'),
        ('reggie', 'Reggie'),
        ('shane and reggie', 'Shane and Reggie'),

    ]

    uu_id = models.UUIDField(default=uuid.uuid4)

    title = models.CharField(max_length=255)
    description = models.TextField()
    release_date = models.DateField()
    tags = models.CharField(max_length=155, choices=CAT_TAGS)
    image_card = models.ImageField(upload_to='cats_images/')
    image_cover = models.ImageField(upload_to='cats_images/')
    video = models.FileField(upload_to='cats_videos/')
    views = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title, self.tags


