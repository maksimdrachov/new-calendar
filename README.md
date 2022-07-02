https://stackoverflow.com/questions/34819221/why-is-python-setup-py-saying-invalid-command-bdist-wheel-on-travis-ci

https://github.com/sajib1066/event-calendar

https://www.youtube.com/watch?v=nTIMYHJRW1c

Setup

```
source my_emv/bin/activate
pip install -r requirements.txt
django-admin startproject eventcalendar .
```

Create app for calendar:

```
python manage.py startapp calendarapp
python manage.py makemigrations
python manage.py migrate
```

Add to installed apps (in `settings.py`):

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'calendarapp.apps.CalendarappConfig',
]
```