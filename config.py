from logging import getLogger

from os import path, pardir, environ as environment

from constants import ENV, DEV_ENV, APP_SECRET, PROD_ENV


class Config(object):
    PROPAGATE_EXCEPTIONS = True
    APP_DIR = path.abspath(path.dirname(__file__))
    PROJECT_ROOT = path.abspath(path.join(APP_DIR, pardir))
    VERSION = '0.1'


class ProductionConfig(Config):
    ENV = PROD_ENV
    DEBUG = False
    SECRET_KEY = environment.get(APP_SECRET)

    DATABASE_CONNECTION = {
        "hostname": "db.prod.ru",
        "port": 8978,
        "database_name": "project_name"
    }


class DevelopmentConfig(Config):
    ENV = DEV_ENV
    DEBUG = True
    SECRET_KEY = environment.get(APP_SECRET, 'bGAAoiY54WOvA0Y63X63DupDvCsZ66J')

    DATABASE_CONNECTION = {
        "hostname": "localhost",
        "port": 5432,
        "database_name": "testdb"
    }
