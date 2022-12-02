from .base import *

import django_on_heroku
from decouple import config
import dj_database_url



from dotenv import load_dotenv, find_dotenv

ALLOWED_HOSTS = ["logicmorph.herokuapp.com", "127.0.0.1"]

SECRET_KEY=config("SECRET_KEY")
EMAIL_HOST = config("EMAIL_HOST")
EMAIL_PORT = config("EMAIL_PORT")
EMAIL_USE_TLS = config("EMAIL_USE_SSL", True)
EMAIL_HOST_USER = config("EMAIL_HOST_USER")
DEFAULT_FROM_MAIL = config("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = config("EMAIL_HOST_PASSWORD")

# UserAuth
AUTH_USER_MODEL = "accounts.User"
LOGIN_URL = config("LOGIN_URL")
LOGOUT_REDIRECT_URL = config("LOGOUT_REDIRECT_URL")
LOGIN_REDIRECT_URL = config("LOGIN_REDIRECT_URL")

# Celery
CELERY_BROKER_URL = config("REDISCLOUD_URL")
CELERY_RESULT_BACKEND = config("REDISCLOUD_URL")


# SALT
HASHID_FIELD_SALT = config("HASHID_FIELD_SALT")

DEBUG = False

# #S3
# AWS_ACCESS_KEY_ID =config("AWS_ACCESS_KEY_ID")
# AWS_SECRET_ACCESS_KEY=config("AWS_SECRET_ACCESS_KEY")
# AWS_STORAGE_BUCKET_NAME=config("AWS_STORAGE_BUCKET_NAME")
# AWS_S3_CUSTOM_DOMAIN= f'{AWS_STORAGE_BUCKET_NAME}.s3.amazon.com'
# AWS_DEFAULT_ACL='public-read'
# AWS_S3_FILE_OVERWRITE =False
# AWS_S3_OBJECT_PARAMETERS ={
# 	'CacheControl': 'max-age=86400'
# }

# DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
# STATICFILES_STORAGE = 'storages.backends.s3boto3.S3StaticStorage'
# AWS_LOCATION = 'static'
# MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/media'

# AWS_QUERYSTRING_AUTH = False

# AWS_HEADERS = {
# 	'Access-Control-Allow-Origin':'*', 
	
# }

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






