__author__ = 'rex'

from django.db import models
from django.contrib.auth.models import User

class Postback(models.Model):
    user_id = models.ForeignKey(User)
    postback_id = models.CharField(max_length=32, unique=True)
    date_created = models.DateTimeField('date created')