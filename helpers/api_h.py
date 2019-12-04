from functools import wraps
from flask import make_response

from dir_app.constants import X_REQUEST_SUCCESS


def add_response_headers(headers):
    def decorator(func):
        @wraps(func)
        def decorated_function(*args, **kwargs):
            response = make_response(func(*args, **kwargs))
            for header, value in headers.items():
                response.headers[header] = value
            return response
        return decorated_function
    return decorator


def x_request_success(func):
    return add_response_headers({X_REQUEST_SUCCESS: True})(func)
