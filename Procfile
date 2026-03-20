web: /opt/venv/bin/gunicorn redneck.wsgi --bind 0.0.0.0:$PORT --workers 2 --timeout 120
release: /opt/venv/bin/python manage.py migrate --noinput && /opt/venv/bin/python manage.py seed_data && /opt/venv/bin/python manage.py create_superuser_if_none && /opt/venv/bin/python manage.py collectstatic --noinput
