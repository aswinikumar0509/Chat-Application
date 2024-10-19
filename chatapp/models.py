from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ChatRoom(models.Model):

    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)


class ChatMessage(models.Model):

    user = models.ForeignKey(User , on_delete=models.CASCADE)
    room = models.ForeignKey(ChatRoom ,on_delete=models.CASCADE)
    message_content = models.TextField()
    data = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('data',)

