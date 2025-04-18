from channels.generic.websocket import WebsocketConsumer,AsyncWebsocketConsumer
import time
from asgiref.sync import async_to_sync
import json
import asyncio


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
        await self.channel_layer.group_add(self.group_name, self.channel_name)
        await self.accept()
    
    async def receive(self, text_data = None, bytes_data=None):
        data = json.loads(text_data)
        message = data.get("message")
        print("dfd.....", self.group_name)
        await self.channel_layer.group_send(self.group_name, {
            "type" : "chat.message",
            "message" : message
        })

    
    async def chat_message(self, event):
        message = event["message"]
        await self.send(text_data=json.dumps({"message": message}))

    
    async def disconnect(self, closed_code):
        print('webscoket disconnected....', closed_code )
        # self.group_name = self.scope.get("url_route").get("kwargs").get("groupname")
        await self.channel_layer.group_discard(self.group_name, self.channel_name)