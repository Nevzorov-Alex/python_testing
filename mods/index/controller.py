import json
import logging
import sys
from http import HTTPStatus

from flask import Blueprint, render_template, render_template_string, make_response, request

mod_index = Blueprint('index', __name__, url_prefix='/')

logger = logging.getLogger(__name__)


@mod_index.route('/', methods=['GET'])
def index_page():
    logger.info('index page')

    return render_template('index.html', code=HTTPStatus.OK)

@mod_index.route('/login', methods=['GET'])
def login():
    logger.info('login page')

    return render_template('login.html', code=HTTPStatus.OK)

@mod_index.route('/auth', methods=['POST'])
def auth_action():
    logger.info('auth_action')
    rec_json=request.json
    email=rec_json.get("email")
    password = rec_json.get("password")
    if email=="aa" and password=="bb":
        return make_response(json.dumps({"text":"Ok"}))
    else:
        return make_response(json.dumps({"text":"Bad!!!"}))

@mod_index.route('/search', methods=['GET'])
def search_page():
    logger.info('search page')

    text = request.args.get("q","")
    d_list=[
        "Apple",
        "Ananas",
        "Banana",
        "Belena",
        "Pineapple",
        "Mango",
    ]

    r_list=[]
    for el in d_list:
        if text in el:
            r_list.append(el)

    return render_template('search.html',data=r_list,query=text, code=HTTPStatus.OK)

@mod_index.route('/registrat', methods=['GET'])
def registrat():
    logger.info('registrat page')

    return render_template('registrat.html', code=HTTPStatus.OK)

@mod_index.route('/reg_auth', methods=['POST'])
def reg_auth_action():
    logger.info('reg_auth_action')
    rec_json=request.json
    log = rec_json.get("login")
    email=rec_json.get("email")
    passw_b = rec_json.get("passw_beg")
    passw_f = rec_json.get("passw_fin")
    if passw_b==passw_f:
        return make_response(json.dumps({"text":"Congatulation you are registered !!!"}))
    else:
        return make_response(json.dumps({"text":"Unfortunately you are not registered !!!"}))
