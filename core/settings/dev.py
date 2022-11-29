from .base import *

DEBUG = True

ALLOWED_HOSTS = ["localhost", "127.0.0.1"]

POSTGRES_ENABLED = get_env_bool("POSTGRES_ENABLED", False)

if not POSTGRES_ENABLED:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql_psycopg2",
            "NAME": os.environ.get("PG_DB_NAME"),
            "USER": os.environ.get("PG_USERNAME"), 
            "PASSWORD": os.environ.get("PG_PASSWORD"),
            "HOST": os.environ.get("PG_HOSTNAME"),
            "PORT": os.environ.get("PG_PORT"),
        }
    }


# #S3
# AWS_ACCESS_KEY_ID ="REMOVED_AWS_KEY_ID"
# AWS_SECRET_ACCESS_KEY="REMOVED"
# AWS_STORAGE_BUCKET_NAME="lm-s3bucket"
# AWS_S3_CUSTOM_DOMAIN= f'{AWS_STORAGE_BUCKET_NAME}.s3.amazon.com'
# AWS_DEFAULT_ACL='public-read'
# AWS_S3_FILE_OVERWRITE =False
# AWS_S3_OBJECT_PARAMETERS ={
# 	'CacheControl': 'max-age=86400'
# }

# DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
# STATICFILES_STORAGE = 'storages.backends.s3boto3.S3StaticStorage'
# # AWS_LOCATION = 'static'


# AWS_QUERYSTRING_AUTH = False

# AWS_HEADERS = {
# 	'Access-Control-Allow-Origin':'*', 
	
# }
# MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/media/'