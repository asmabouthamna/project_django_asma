import  json 

from mqttasgi.consumers import MqttConsumer
from persistance.persistance_engine import persist_data

class GrandeurMqttConsumer(MqttConsumer):
    
    async def connect(self):
        await self.subscribe('sensor/temperature' ,2)
        print('MQTT connected....')
        self.room_group_name = 'sensor_temperature'
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)

    async def receive(self, mqtt_message):
        print(f'Received message topic: {mqtt_message['topic']}')
        print(f'with payload {mqtt_message['payload']}')
        print(f'And Qos {mqtt_message['qos']}')
        await self.channel_layer.group.send(
            self.room_group_name,
            {
                "type":"sensor.temperature",
                "message":{"payload": mqtt_message['payload'].decode("utf-8")}
            }
        )
    async def sensor_temperature(self, event):
        message = event["message"]
        persist_data(message['payload'])
        
    async def disconnect(self):
        await self.unsubscribe('sensor/temperature')