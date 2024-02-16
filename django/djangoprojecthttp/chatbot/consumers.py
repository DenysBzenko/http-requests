from channels.generic.websocket import AsyncConsumer
import json

class YourConsumer(AsyncConsumer):
    async def websocket_connect(self, event):
        await self.send({"type": "websocket.accept"})

    async def websocket_receive(self, text_data):
        message = json.loads(text_data)
        await self.send_group(message)

    async def websocket_disconnect(self, event):
        pass

    async def send_group(self, message):
        await self.channel_layer.group_add('chat', self.channel_name)
        await self.channel_layer.group_send(
            'chat',
            {
                'type': 'chat.message',
                'message': message,
            }
        )

    async def chat_message(self, event):
        message = event['message']
        await self.send({
            "type": "websocket.send",
            "text": json.dumps(message),
        })
