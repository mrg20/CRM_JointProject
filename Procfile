release: python manage.py makemigrations && python manage.py migrate --no-input
web: gunicorn CRM.wsgi --log-file -
