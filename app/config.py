
import os
from app.networks import get_ip


class Config(object):
    APPLICATION_DIR = os.path.dirname(os.path.realpath(__file__))
    STATIC_DIR = os.path.join(APPLICATION_DIR, 'static')
    IMAGES_DIR = os.path.join(APPLICATION_DIR, 'images')
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    DEBUG = True
    TESTING = True

    # connection to mysql (local/server)  db configuration
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'mysql://bob:secret@{}/testF'.format(get_ip())      
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    ADMIN = os.environ.get('ADMIN') or "ahmnouira@gmail.com"
    # ADMIN_PASSWORD = 'aze'
    # ROLES = ["admin", "user"]

    # mySQL database configuration for docker
    MYSQL_RANDOM_ROOT_PASSWORD = os.environ.get('MYSQL_RANDOM_ROOT_PASSWORD') or "yes"
    MYSQL_DATABASE = os.environ.get('MYSQL_DATABASE') or "iot_platform_db"
    MYSQL_USER = os.environ.get('MYSQL_USER') or "iot_platform"
    MYSQL_PASSWORD = os.environ.get('MYSQL_PASSWORD') or "secret"






