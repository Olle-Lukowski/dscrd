import requests

class Webhook:
    def __init__(self, id: str):
        self.url = "https://discord.com/api/webhooks/" + id

    def send_message(self, message: str, tts: bool = False, embeds: list = None, allowed_mentions: dict = None, message_reference: dict = None):
        """Send a message to the webhook."""
        data = {
            "content": message,
            "tts": tts,
            "embeds": embeds,
            "allowed_mentions": allowed_mentions
            "message_reference": message_reference
        }
        return requests.post(self.url, json=data)
    

