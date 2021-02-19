from django.db import models
from django.urls import reverse
from django.utils import timezone

from users.models import User


class Event(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    time = models.DateTimeField()
    address = models.CharField(max_length=100)
    completed = models.CharField(max_length=30, default="uncompleted")
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('event-detail', args=(self.id,))

    @property
    def get_html_url(self):
        url = reverse('event-detail', args=(self.id,))
        if self.completed == 'completed' :
            return f'<a href="{url}" style="text-decoration:line-through"> {self.title} </a>'
        else:
            return f'<a href="{url}"> {self.title} </a>'