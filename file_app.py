import logging
import os
from pprint import pprint

from flask import Flask, Blueprint, redirect, url_for
#from flask_cors import CORS
#from flask_restful import Api

from constants import X_REQUEST_SUCCESS, ANY_ORIGIN, DEV_ENV, ENV, PROD_ENV

from config import DevelopmentConfig, ProductionConfig

from exceptions import BaseAppException

# Logger configuration
from helpers.flask_h import app_exception_handler, \
    uncaught_exception_handler

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Configuration initialization
env_var = os.environ.get(ENV)
if env_var is None:
    logger.fatal(f'* Environment variable is missing: {ENV}')
    exit(1213)

config = None
if env_var == 'DEV_ENV':
    config = DevelopmentConfig()
elif env_var == 'PROD_ENV':
    config = ProductionConfig()
else:
    logger.fatal(f'* Environment variable has wrong value: {env_var}')
    exit(1214)

logger.info(f'* Config type: {env_var.capitalize()}')

flask_app = Flask(__name__)
flask_app.jinja_env.add_extension('jinja2.ext.loopcontrols')
flask_app.url_map.strict_slashes = False
# url: /api/resource/id/ --> /api/resource/id
flask_app.config.from_object(config)

# api_bp = Blueprint("/api", __name__)
# api = Api(api_bp)
#
# flask_app.register_blueprint(api_bp)

from mods.index.controller import mod_index

flask_app.register_blueprint(mod_index)

# Exception handlers registration
flask_app.errorhandler(BaseAppException)(app_exception_handler)

if config.ENV != DEV_ENV:
    flask_app.errorhandler(Exception)(uncaught_exception_handler)

pprint(flask_app.url_map._rules_by_endpoint)

if __name__ == '__main__':
    flask_app.run(host="localhost", port=8081, debug=True)
