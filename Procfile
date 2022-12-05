# web: gunicorn core.wsgi --log-file -
web: daphne core.asgi:application --port $PORT --bind 0.0.0.0 -v2
celery: celery -A core.celery worker --pool=solo -l info -v2