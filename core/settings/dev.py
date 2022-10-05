from .base import *

DEBUG = True

ALLOWED_HOSTS = ["localhost", "127.0.0.1"]

POSTGRES_ENABLED = get_env_bool("POSTGRES_ENABLED", False)

if not POSTGRES_ENABLED:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db2.sqlite3",
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
        # "default": {
        #     "ENGINE": "django.db.backends.postgresql_psycopg2",
        #     "NAME": "logicmorphdb",
        #     "USER": "postgres",
        #     "PASSWORD": "logicmorph2022",
        #     "HOST": "127.0.0.1",
        #     "PORT": "5432",
        # }
    }


#CELERY SETTINGS
CELERY_BROKER_URL           = 'redis://127.0.0.1:6379'
CELERY_ACCEPT_CONTENT       = ['application/json']
CELERY_RESULT_SERIALIZER    = 'json'
CELERY_TASK_SERIALIZER      = 'json'
CELERY_TIMEZONE             = 'Asia/Manila'

CELERY_RESULT_BACKEND       = 'django-db'
CELERY_RESULT_BACKEND       = 'django-db'
CELERY_CACHE_BACKEND        = 'django-cache'

#CELERY BEAT
CELERY_BEAT_SCHEDULER       =  'django_celery_beat.schedulers:DatabaseScheduler'