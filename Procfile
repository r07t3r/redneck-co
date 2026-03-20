web: gunicorn redneck.wsgi --bind 0.0.0.0:$PORT --workers 2 --timeout 120
release: python manage.py migrate --noinput && python manage.py seed_data && python manage.py create_superuser_if_none && python manage.py collectstatic --noinput
