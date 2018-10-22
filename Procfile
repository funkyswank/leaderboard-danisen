release: python manage.py migrate
web: waitress-serve --listen=0.0.0.0:$PORT FPDanisen.wsgi:application