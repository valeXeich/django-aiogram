release: python backend/manage.py makemigrations
release: python backend/manage.py migrate
web: gunicorn --bind 0.0.0.0:8002 backend.config.wsgi