release: python backend/manage.py makemigrations
release: python backend/manage.py migrate
web: gunicorn config.wsgi:application