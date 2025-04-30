from channels.generic.websocket import WebsocketConsumer,AsyncWebsocketConsumer
import time
from asgiref.sync import async_to_sync
import json
import asyncio
from django.template.loader import get_template
from .services import save_message
from django.core.cache import cache

class MyWebsocketConsumer(WebsocketConsumer):
    def connect(self):
        # print('websocket connected...')
        self.group_name = self.scope['url_route']['kwargs']["groupname"]
        # print(self.group_name)
        async_to_sync(self.channel_layer.group_add)(
            self.group_name,
            self.channel_name
        )
        self.accept()
    
    def receive(self, text_data = None, bytes_data=None):
        # print('Message recieved ...', text_data)
        self.group_name = self.scope['url_route']['kwargs']["groupname"]
        data = json.loads(text_data)
        message = data['message']
        async_to_sync(self.channel_layer.group_send)(
            self.group_name,
            {
                'type' : 'chat.message',
                'message':message
            }
        )
    
    def chat_message(self,event):
        self.send(text_data=json.dumps({
            "message" : event['message']
        }))

        # async_to_sync(self.channel_layer.s)
    def disconnect(self, closed_code):
        print('webscoket disconnected....', closed_code )
        async_to_sync(self.channel_layer.group_discard)(self.group_name, self.channel_name)



class MyAsyncWebsocketConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        print('websocket connected...')
        self.group_name = self.scope.get("url_route").get("kwargs").get("groupname")
        self.user = self.scope.get('user')
        await self.channel_layer.group_add(self.group_name, self.channel_name)
        if self.user.is_authenticated:
            await self.set_user_online(self.user.id)
        await self.accept()
    
    async def receive(self, text_data = None, bytes_data=None):
        data = json.loads(text_data)
        message = data.get("message")
        user = self.scope.get('user')
        other_user = await save_message(sender = user, message = message, group_id = self.group_name)
        html = get_template("rightbar/partials/chatText.html").render(context={'message': message})
        # self.send(text_data=html)
        await self.channel_layer.group_send(self.group_name, {
            "type" : "chat.message",
            "message" : html
        })

    
    async def chat_message(self, event):
        message = event["message"]
        await self.send(text_data=message)

    
    async def disconnect(self, closed_code):
        print('webscoket disconnected....', closed_code )
        await self.set_user_offline(self.user.id)
        # self.group_name = self.scope.get("url_route").get("kwargs").get("groupname")
        await self.channel_layer.group_discard(self.group_name, self.channel_name)
    
    async def set_user_online(self, user_id):
        # Store a simple key in Redis
        cache.set(f"user_online_{user_id}", True, timeout=None)

    async def set_user_offline(self, user_id):
        cache.delete(f"user_online_{user_id}")
