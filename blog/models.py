from email.policy import default
from django.db import models

class Fitnessgraph(models.Model):
    class ActiveMetz():
        metz3 = 3
        metz4 = 4
        metz5 = 5
    ACTIVE_CHOICE = (
        (ActiveMetz.metz3,'体操'),
        (ActiveMetz.metz4,'卓球'),
        (ActiveMetz.metz5,'野球'),
    )
    active = models.CharField(choices=ACTIVE_CHOICE,
                            max_length=100,)
    time = models.IntegerField(blank=True, null=True)
    day = models.DateField()

    def __str__(self):
        return self.active

class Fitnesspulldown(models.Model):
    active = models.CharField(max_length=100)
    metz = models.FloatField(default=0)