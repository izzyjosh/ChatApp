from django.urls import path
from . import views

app_name = "main"
urlpatterns = [
        path("",views.index,name="index"),
        path("chatroom/<slug:slug>/",views.chatroom,name="chatroom"),
        ]
