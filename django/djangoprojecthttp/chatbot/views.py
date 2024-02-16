from django.http import JsonResponse, HttpResponse
from .helpers.cookie_helpers import set_cookie, get_cookie
from .helpers.header_helpers import set_header, get_header
from .helpers.utils import load_users, save_users
import json
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render

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

@csrf_exempt
def get_all_users(request):
    users = load_users()
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
def post_user(request):
    users = load_users()
    new_user = json.loads(request.body)
    users.append(new_user)
    save_users(users)
    return JsonResponse(new_user, status=201)
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
