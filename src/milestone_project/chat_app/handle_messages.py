import requests
from datetime import datetime


class HandleMessages:
    def __init__(self):
        self.messages = []

    def get_messages(self):
        messages = requests.get("http://167.99.63.70/messages").json()
        messages = self.format_messages(messages)
        return messages

    def format_messages(self, messages):
        for index, message in enumerate(messages):
            message["date"] = datetime.fromtimestamp(
                message["date"]
            ).strftime("%d-%m-%Y %H:%M:%S")
            messages[index] = message
        return messages

    def send_message(self, message):
        requests.post(
            "http://167.99.63.70/message", json={"message": message}
        )
