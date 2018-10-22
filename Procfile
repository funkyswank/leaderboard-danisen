release: python manage.py migrate
web: waitress-serve --port=$PORT --host=0.0.0.0 FPDanisen.wsgi:application