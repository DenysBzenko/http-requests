def set_cookie(response, cookie_name, cookie_value, http_only=True):
    response.set_cookie(cookie_name, cookie_value, httponly=http_only)

def get_cookie(request, cookie_name):
    return request.COOKIES.get(cookie_name, 'Cookie not found')
