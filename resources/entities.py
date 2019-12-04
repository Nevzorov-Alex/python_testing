import time

from dir_app.file_app import api

from flask_restful import Resource
from dir_app.constants import ENTITY, LOCATION

from flask import jsonify, request, make_response
from dir_app.helpers.api_h import x_request_success

from http import HTTPStatus

__all__ = [
    'Services'
]

a = "83b4e1be-8451-48be-867b-2399bfdddac5"
b = "1a12e5ab-77f2-467b-a33b-0549ef98c4f"

data = [
    {
        "uuid": a,
        "status": 1,
        "name": "this is so shit service",
        "lang": "python",
        "description": "Some loooong description because it can be so long "
                       "escription as fucking Lev tolstoi Voina i mir book",
        "version": "1",
        "is_systemd": False,
        "created_date": time.time(),
        "modify_date": time.time(),
        "modify_reason": "no reason",
    },
    {
        "uuid": b,
        "status": 4,
        "name": "new brand service",
        "lang": "",
        "description": "just short description",
        "version": "0.0.1",
        "is_systemd": True,
        "created_date": time.time(),
        "modify_date": time.time(),
        "modify_reason": "This is more seriously!",
    }
]

@api.resource(f'/{ENTITY}')
class Services(Resource):
    __slots__ = 'api'

    def __init__(self):
        pass

    @x_request_success
    def post(self):
        r = make_response(jsonify(''), HTTPStatus.CREATED)
        return r

    @x_request_success
    def get(self):
        return make_response(jsonify(data))
