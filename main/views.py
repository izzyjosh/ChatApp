from django.shortcuts import render,redirect
from django.http import HttpRequest
from .models import ChatRoom,Message
from django.contrib.auth.decorators import login_required


@login_required
def index(request:HttpRequest):

    chatrooms = ChatRoom.objects.all()
    context = {"chatrooms":chatrooms}
    return render(request,"main/index.html",context)


@login_required
def chatroom(request:HttpRequest,slug):
    chatroom = ChatRoom.objects.get(slug=slug)
    messages = Message.objects.filter(receiver=chatroom)

    context = {"chatroom":chatroom,"messages":messages}
    return render(request,"main/chatroom.html",context)
