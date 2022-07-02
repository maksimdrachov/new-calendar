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
    'calendarapp',
]
```

Create model in calendarapp:

```python
class EventAbstract(models.Model):
    """ Event abstract model """

    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Event(EventAbstract):
    """ Event model """

    #user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="events")
    title = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    #objects = EventManager()

    # def __str__(self):
    #     return self.title

    # def get_absolute_url(self):
    #     return reverse("calendarapp:event-detail", args=(self.id,))

    # @property
    # def get_html_url(self):
    #     url = reverse("calendarapp:event-detail", args=(self.id,))
    #     return f'<a href="{url}"> {self.title} </a>'
```

Add to admin.py:

```python
from .models import Event

admin.site.register(Event)
```

Create a view in eventcalendar:



