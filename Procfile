web: gunicorn core.wsgi --log-file -

web: daphne clannels_celery_heroku_project.asgi.:application --port $PORT --bind 0.0.0.0 -v2
celery: celery -A channels_celery_heroku_project worker --pool=solo -l info