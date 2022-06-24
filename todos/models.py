from email import contentmanager
from django.db import models

# Create your models here.

class Todo(models.Model):
    id = models.AutoField(primary_key=True)
    start_time = models.TimeField()
    end_time = models.TimeField()
    content = models.CharField(max_length=200)
    is_done = models.BooleanField(default=False)