import datetime
from django.db import models

class Feedback(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=255)
    message = models.TextField()
    from_email = models.EmailField()
    create_date = models.DateField(default=datetime.datetime.now())
