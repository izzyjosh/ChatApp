import json
from django.shortcuts import get_object_or_404
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from main.models import ChatRoom,Message
from django.contrib.auth import get_user_model
User = get_user_model()


class ChatRoomConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = f"chat_{self.room_name}"

        await self.channel_layer.group_add(
                self.room_group_name,
                self.channel_name
                )
        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)


    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data["message"]
        username = data["username"]
        room = data["room"]

        await self.save_message(username,room,message)

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name, {
                "type": "chat_message", 
                "message": message,
                "username":username,
                "room":room
                }
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event["message"]
        username = event["username"]
        room = event["room"]

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            "message": message,
            "username":username,
            "room":room
            }))

    @database_sync_to_async
    def save_message(self,username,room,message):
        sender = User.objects.get(username=username)
        room = ChatRoom.objects.get(slug=room)

        Message.objects.create(sender=sender,receiver=room,message=message)
