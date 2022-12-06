web: gunicorn core.wsgi --log-file -
# celery: celery -A core.celery worker --pool=solo -l info
# celerybeat: celery -A core beat -l INFO
# web: daphne core.asgi:application --port $PORT --bind 0.0.0.0 -v2
# celeryworker: celery -A core.celery worker & celery -A core beat --pool=solo -l INFO & wait -n
celerycelerybeat: celery -A core.celery worker --pool=solo -l info & celery -A core beat -l INFO & wait -n

