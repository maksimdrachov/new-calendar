from django.db import models

# Create your models here.
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