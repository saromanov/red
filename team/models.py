from django.contrib.auth.models import User
from django.db import models
from location_field.models.plain import PlainLocationField

class Profile(User):
    status = models.CharField(max_length=20)
    description = models.CharField(max_length=500)
    position = models.CharField(max_length=50)
    contact = models.CharField(max_length=50)
    birthday = models.DateTimeField('birthday')
    location = PlainLocationField(based_fields=['city'], zoom=7)
    def __str__(self):
        return '{0} {1}'.format(self.first_name, self.last_name)

class Team(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return name

