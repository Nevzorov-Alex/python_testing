from functools import wraps
from http import HTTPStatus
from logging import getLogger

from flask import make_response
from flask.json import jsonify

from traceback import format_exc

from constants import X_REQUEST_SUCCESS
from exceptions import AppException


def app_exception_handler(exception):
    r = make_response(jsonify({
        'message': exception.message,
        'code': exception.code
    }), HTTPStatus.INTERNAL_SERVER_ERROR)  # FIXME
    r.headers[X_REQUEST_SUCCESS] = False
    return r


def uncaught_exception_handler(exception):
    getLogger(__name__).error(
        f'* Uncaught exception [{exception}]: {format_exc()}')
    return app_exception_handler(AppException(message="", code=1))  # FIXME


def authenticate(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not getattr(func, 'authenticated', True):
            return func(*args, **kwargs)
        # acct = basic_authentication()  # TODO
        if True:
            return func(*args, **kwargs)
        restful.abort(HTTPStatus.UNAUTHORIZED)

    return wrapper

