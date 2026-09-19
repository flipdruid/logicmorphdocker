# CLAUDE.md — logicmorphdocker

Django web app (company site + client/lead portal) run with Docker Compose.
Repo: `git@github.com:flipdruid/logicmorphdocker.git` — working branch `feature/docker3`, published as `main`.

## Working rules

- **Consult before changing anything.** Propose the fix, wait for approval.
- **One file at a time.** Deliver complete files, always with the destination path.
- **Never bundle bug fixes with design/refactor changes.** Separate commits.
- Keep explanations concise. Developer is on Windows using **Git Bash (MINGW64)**.

## Stack

- Python 3.8 (`python:3.8-alpine` image), Django 4.1.1
- PostgreSQL 16 (pinned — do not use unpinned `postgres`; 18+ changed the data layout)
- Redis + Celery 5.2.7 (worker), django-celery-beat 2.4.0 (DatabaseScheduler)
- django-registration, crispy-forms (bootstrap4), widget-tweaks, django-fsm, django-hashid-field, whitenoise
- Templates: SB Admin–based dashboard in `templates/`

## Layout

```
core/            project: settings/{base,dev,prod}.py, urls.py, celery.py
accounts/        custom User (AUTH_USER_MODEL = accounts.User), auth views, signals
app/             main app: models/, views/, forms/, tasks/, tests/, context/
templates/       all templates (main/, accounts/, dashboard/, django_registration/)
static/, media/  assets; default avatars at media/avatar/logicmorph0-9.png
```

- Default settings module: `core.settings.dev` (manage.py, celery.py, asgi.py).
- `prod.py` is Heroku-era config (django_on_heroku, dj_database_url) — not used by Docker.
- URLs: `/` landing, `/portal/` app, `/accounts/` auth, `/lm-super-admin/` admin.
- Primary keys are Hashids (`HashidAutoField`) → URL params are `<str:pk>`.

## Docker services

| Service | Container | Notes |
|---|---|---|
| app | `django_app` | runs `migrate` then `runserver 0.0.0.0:8000` |
| db | `postgres_db` | volume `logicmorphdocker_pgdata` |
| redis | `redis` | broker `redis://redis:6379/0` |
| celery | `celery` | `celery -A core worker` — **does not auto-reload** |

Project folder is mounted at `/django`, so code changes are live — no rebuild needed.

## Commands

```bash
docker-compose up                      # start
docker-compose build --no-cache        # only after requirements.txt / Dockerfile changes
docker-compose restart celery          # after Python code changes

docker exec -it django_app python manage.py check
docker exec -it django_app python manage.py test
docker exec -it django_app python manage.py makemigrations   # run manually, never on startup
docker exec -it django_app python manage.py migrate
docker exec -it django_app python manage.py createsuperuser
```

Git Bash rewrites `/paths` in docker args — prefix with `MSYS_NO_PATHCONV=1` when needed.

## Config

`.env` (gitignored) holds: `POSTGRES_ENABLED`, `PG_*` (host `db`), `EMAIL_*`,
`LOGIN_URL` / `LOGIN_REDIRECT_URL` / `LOGOUT_REDIRECT_URL`, `HASHID_FIELD_SALT`,
`CELERY_BROKER_URL` / `CELERY_RESULT_BACKEND`. Template: `.env.sample`.
Never commit secrets — GitHub push protection is on (AWS keys were purged from history).

## Gotchas

- **Model defaults must be callables, not expressions.** `Profile.avatar` uses `default_avatar()`;
  an inline `random.choice(...)` default caused a new migration on every `makemigrations`.
- **`Lead.save()` uses `celery.current_app.send_task(...)`**, which always goes to Redis and
  ignores `CELERY_TASK_ALWAYS_EAGER`. Tests stub it with `mock.patch("celery.current_app")`.
- `accounts/signals.py` creates the `admin` / `staff` / `client` groups and a Profile on user creation.
- Many `*backup*.html` templates exist — the live one is the name without a suffix.

## Status

Done: Django pin restored, PyYAML 6.0.1, celery-beat 2.4.0, postgres:16 pinned,
compose env quotes fixed, makemigrations removed from startup, avatar migration churn fixed
(0024 + 0025), unused `import imp` removed, lead tests fixed (48/48 passing).

Open (in priority order):
1. `Lead.save()` queues the contact email on **every** save, not only on create.
2. Hardcoded `SECRET_KEY` in `core/settings/base.py` → move to `.env`.
3. Broken `LOGGING` dict in `core/settings/prod.py` (handlers nested in formatters, format typos).
4. Cleanup: backup templates, `docker-compose copy.yml`, `db.sqlite3`, obsolete `version:` in
   compose, duplicate media/static `serve` routes in `app/urls.py` and `accounts/urls.py`,
   EOL Python 3.8 base image.
