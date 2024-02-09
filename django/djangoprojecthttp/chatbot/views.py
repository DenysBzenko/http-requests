from django.http import JsonResponse
from .helpers.cookie_helpers import set_cookie, get_cookie
from .helpers.header_helpers import set_header, get_header


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
