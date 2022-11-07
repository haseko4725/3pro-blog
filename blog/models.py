from email.policy import default
from django.db import models

class Fitnesspulldown(models.Model):
    active = models.CharField(max_length=100,blank=True)
    metz = models.FloatField(default=0)

class Fitnessgraph(models.Model):
    active = models.ForeignKey(Fitnesspulldown, on_delete=models.SET_NULL, null=True)
    time = models.IntegerField(blank=True, null=True)
    day = models.DateField()
