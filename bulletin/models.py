from django.db import models

# Create your models here.

class Board(models.Model):
    title = models.CharField(max_length=30)
    time = models.DateTimeField()
    address = models.CharField(max_length=50)
    content = models.TextField(null=True, blank=True)
    completed = models.CharField(max_length=10)
    writer = models.CharField(max_length=30)