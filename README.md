# LOGICMORPH Website

This website is built with [Django](https://www.djangoproject.com/) and [Bootstrap](https://getbootstrap.com/). We use [pre-commit](https://pre-commit.com/) to handle commit and get a nice formatting for the code and [djlint](https://www.djlint.com/) for formatting the templates.

### Requirements:

* [Python 3.8.10](https://www.python.org/downloads/)
* virtualenv
* [Postgres](https://www.postgresql.org/)

### Local Setup

Setup your virtualenvironment first using the required python version.

#### Setting up your local environment
Copy `.env.sample` and create new file named `.env` to use the environment variable. It is recommended to setup your local Postgres instance first. The project defaults to sqlite currently if the environment variables found in `.env.sample` aren't present.

Install dependencies
```
[logicmorph] pip install -r requirements.txt
```
Run migrations
```
[logicmorph] python manage.py migrate
```
Run the website
```
[logicmorph] python manage.py runserver
```

### Commits
When doing commits, make sure that all the `pre-commit` checks passes before pushing it in a branch because it will unstage new changes.

### DJlint

Always reformat the html files that you are working on before doing commits so that the templates would look nicely formatted.

Run djlint

```
[logicmorph] djlint --reformat templates/path/to/your.html
```


### Run Celery using terminal

#### Run celery with multiple workers
```
[logicmorph]  celery -A core.celery worker -l info
```
#### Run celery with single worker
```
[logicmorph] celery -A core.celery worker --pool=solo -l info
```
#### Run celery with worker at your choice
```
[logicmorph] celery -A core.celery worker --concurrency=5 -l info
```

