web: gunicorn core.wsgi --log-file -
celery: celery -A core.celery worker --pool=solo -l info
# web: daphne core.asgi:application --port $PORT --bind 0.0.0.0 -v2
# celery: celery -A core.celery worker & celery -A core beat --pool=solo -l INFO & wait -n

