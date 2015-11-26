from django.db import models
from django.contrib.auth.models import User

class Coach(models.Model):
    GENDERS = (('M', 'Mail'), ('F', 'Femail'),)
    user = models.OneToOneField(User)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDERS)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    skype = models.CharField(max_length=30)
    description = models.TextField()

    def __unicode__(self):
        return self.user.first_name
