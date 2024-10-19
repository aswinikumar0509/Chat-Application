from django.db import models

# Create your models here.

class ChatRoom(models.Model):

    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    
