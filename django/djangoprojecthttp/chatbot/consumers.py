from channels.generic.websocket import AsyncWebsocketConsumer
import json

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add(
            "chat",  # Група для всіх з'єднань, оскільки ми не використовуємо кімнати
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            "chat",
            self.channel_name
        )

    async def receive(self, text_data=None, bytes_data=None):
        text_data_json = json.loads(text_data)
        message = text_data_json.get('message')

        # Відправлення повідомлення всім учасникам групи
        await self.channel_layer.group_send(
            "chat",
            {
                'type': 'chat_message',
                'message': message
            }
        )

    # Прийняття повідомлення з групи
    async def chat_message(self, event):
        message = event['message']

        # Відправлення повідомлення назад до WebSocket
        await self.send(text_data=json.dumps({
            'message': message
        }))
