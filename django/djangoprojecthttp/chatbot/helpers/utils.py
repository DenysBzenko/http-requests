import json
from django.conf import settings
import os

def load_users():
    with open(os.path.join(settings.BASE_DIR, 'chatbot', 'data', 'users.json'), 'r') as file:
        return json.load(file)

def save_users(users):
    with open(os.path.join(settings.BASE_DIR, 'chatbot', 'data', 'users.json'), 'w') as file:
        json.dump(users, file, indent=4)
