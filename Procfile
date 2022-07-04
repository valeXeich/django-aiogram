release: python backend/manage.py makemigrations
release: python backend/manage.py migrate
worker: python backend/manage.py bot_run
web: python backend/manage.py runserver 0.0.0.0:$PORT