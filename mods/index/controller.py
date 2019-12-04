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