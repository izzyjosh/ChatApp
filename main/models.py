from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

class ChatRoom(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

class Message(models.Model):
    sender = models.ForeignKey(User,on_delete=models.CASCADE,related_name="sender")
    message = models.TextField()
    receiver = models.ForeignKey(ChatRoom,on_delete=models.CASCADE,related_name="reveiver")
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message

    class Meta:
        ordering = ("date",)

