release: python backend/manage.py makemigrations
release: python backend/manage.py migrate
web: gunicorn $WSGI_PATH:application --log-file=-