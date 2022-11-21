from .base import *

import django_on_heroku
from decouple import config



from dotenv import load_dotenv, find_dotenv

ALLOWED_HOSTS = ["logicmorphdevs.herokuapp.com", "127.0.0.1"]

SECRET_KEY=config("SECRET_KEY")

DEBUG = False

load_dotenv(find_dotenv())

import dj_database_url

DATABASES = {
    "default": dj_database_url.config(default='sqlite://db.sqlite3', 
    conn_max_age=600, ssl_require=False)
}





LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': "[%(astime)s]%(develname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt': "%d/%b/%Y %H:%M:%S"
        },
        'simple' : {
            'format': '%(levelname)s %(message)s'
        },
        'handlers': {
            'console': {
                'level': 'DEBUG',
                'class':'logging.StreamHandler',
            },
            'loggers': {
                'MYAPP': {
                    'handlers': ['console'],
                    'level': 'DEBUG',
                }
            }
        }
    }

}

#Heroku Settings
django_on_heroku.settings(locals(),staticfiles=False)

del DATABASES['default']['OPTIONS']['sslmode']






