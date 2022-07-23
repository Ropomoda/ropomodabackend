#!/bin/bash

SUPERUSER_MOBILE=${DJANGO_SUPERUSER_MOBILE}
cd /app/

/opt/venv/bin/python3 manage.py migrate --noinput
/opt/venv/bin/python3 manage.py createsuperuser --mobile $SUPERUSER_MOBILE --noinput || true

