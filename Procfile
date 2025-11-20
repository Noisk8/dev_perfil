web: python manage.py collectstatic --noinput && python manage.py migrate --noinput && gunicorn perfil_noisk8.wsgi:application --bind 0.0.0.0:${PORT:-8000}
