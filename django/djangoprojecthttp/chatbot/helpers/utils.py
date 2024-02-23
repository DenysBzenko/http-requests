import json


def load_users():
    with open('users.json', 'r', encoding='utf-8') as file:
        return json.load(file)

def save_users(users):
    with open('users.json', 'w', encoding='utf-8') as file:
        json.dump(users, file, indent=4)
