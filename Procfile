release: python backend/manage.py makemigrations
release: python backend/manage.py migrate
web: gunicorn backend.config.wsgi --log-file=-