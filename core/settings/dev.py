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
