from django.db import models
from django.urls import reverse
# Create your models here.


class Todo(models.Model):
    username = models.TextField(max_length=100)
    item = models.TextField(max_length=200)
    complete = models.BooleanField(default=False)



