from django.http import JsonResponse, HttpResponse
from .helpers.cookie_helpers import set_cookie, get_cookie
from .helpers.header_helpers import set_header, get_header
from .helpers.utils import load_users, save_users
from django.shortcuts import render
from django.http import JsonResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
import json
import datetime
from pymongo import MongoClient
import logging

logger = logging.getLogger(__name__)

client = MongoClient('mongodb+srv://dbzenko:pppp@cluster0.ntu0tgk.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
db = client['my_database']
users_collection = db['users']


def set_cookie_view(request):
    name = request.GET.get('name')
    value = request.GET.get('value')
    response = JsonResponse({'message': f'Cookie : {name} = {value}'})
    set_cookie(response, name, value)
    return response


def get_cookie_view(request, name):
    value = get_cookie(request, name)
    return JsonResponse({name: value})


def set_header_view(request):
    name = request.GET.get('name')
    value = request.GET.get('value')
    response = JsonResponse({'message': f'Header : {name} = {value}'})
    set_header(response, name, value)
    return response


def get_header_view(request, name):
    value = get_header(request, name)
    return JsonResponse({name: value})

def get_all_users(request):
    users = list(users_collection.find({}))
    return JsonResponse(users, safe=False)

@csrf_exempt
def get_user_by_id(request, id):
    users = load_users()
    user = next((user for user in users if user['id'] == id), None)
    if user:
        return JsonResponse(user)
    else:
        return HttpResponse(status=404)

@csrf_exempt
def register(request):
    if request.method == 'POST':
        new_user = {
            "username": request.POST.get('username'),
            "email": request.POST.get('email'),
            "first_name": request.POST.get('first_name'),
            "last_name": request.POST.get('last_name'),
            "profession": request.POST.get('profession'),
            "created_at": datetime.now(),
            "is_admin": False
        }
        users_collection.insert_one(new_user)
        return HttpResponseRedirect(reverse("my_websocket"))
    else:
        return render(request, 'registration.html')

@csrf_exempt
def put_user(request, id):
    users = load_users()
    user_index = next((index for index, user in enumerate(users) if user['id'] == id), None)
    if user_index is None:
        return HttpResponse(status=404)
    user_data = json.loads(request.body)
    users[user_index] = user_data
    save_users(users)
    return JsonResponse(user_data)

@csrf_exempt
def patch_user(request, id):
    users = load_users()
    user = next((user for user in users if user['id'] == id), None)
    if not user:
        return HttpResponse(status=404)
    user_data = json.loads(request.body)
    user.update(user_data)
    save_users(users)
    return JsonResponse(user)

@csrf_exempt
def delete_user(request, id):
    users = load_users()
    user = next((user for user in users if user['id'] == id), None)
    if not user:
        return HttpResponse(status=404)
    users.remove(user)
    save_users(users)
    return HttpResponse(status=204)

@csrf_exempt
def get_admin_users(request):
    users = load_users()
    admin_users = [user for user in users if user.get('is_admin')]
    return JsonResponse(admin_users, safe=False)


def my_websocket(request):
    return render(request, 'websocket.html')
