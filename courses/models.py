from django.db import models
from coaches.models import Coach

class Course(models.Model):
    name = models.CharField(max_length=75)
    short_description = models.CharField(max_length=100)
    description = models.TextField()
    coach = models.ForeignKey(Coach, related_name='coach_courses')
    assistant = models.ForeignKey(Coach, related_name='assistant_courses')

    def __unicode__(self):
        return self.name

class Lesson(models.Model):
    subject = models.CharField(max_length=200)
    description = models.TextField()
    course = models.ForeignKey(Course)
    order = models.PositiveIntegerField()

    def __unicode__(self):
        return self.subject
