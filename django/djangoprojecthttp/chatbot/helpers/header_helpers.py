def set_header(response, header_name, header_value):
    response[header_name] = header_value

def get_header(request, header_name):
    return request.headers.get(header_name, 'Header not found')
