from channels.generic.websocket import AsyncWebsocketConsumer
import json
class DashboardConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        print('connect....')
        await self.accept()
        await self.send(text_data=json.dumps({"message": 'connected..'}))
        self.room_group_name = 'sensor_temperature'
        await self.channel_layer.group_add(self.room_group_name,self.channel_name)
    async def sensor_temperature(self,event):
        message = event["message"] 
        await self.send(text_data=json.dumps({"message":message['payload']}))

    async def receive(self,mqtt_message):
        pass

    async def disconnect(self , close_code):
        pass