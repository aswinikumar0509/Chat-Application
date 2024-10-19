from django.shortcuts import render
from .models import ChatRoom

# Create your views here.

def index(request):
    chatroom = ChatRoom.objects.all()
    return render(request , 'chatapp/index.html',{'chatroom':chatroom})

def chatroom(request,slug):
    chatroom = ChatRoom.objects.get(slug=slug)
    return render(request,'chatapp/room.html',{'chatroom':chatroom})