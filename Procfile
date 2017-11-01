release: python manage.py migrate && python manage.py collectstatic --noinput
web: waitress-serve --port=$PORT config.wsgi:application
