web: gunicorn core.wsgi --log-file -
celery: celery -A channels_celery_heroku_project worker --pool=solo -l info