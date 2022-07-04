release: python backend/manage.py makemigrations
release: python backend/manage.py migrate
release: python backend/manage.py createadmin
worker: python backend/manage.py bot_run
web: python backend/manage.py runserver 0.0.0.0:$PORT