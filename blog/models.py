from django.db import models

class Fitnessgraph(models.Model):
    #active = models.CharField(max_length=100)
    metz = models.IntegerField(blank=True, null=True)
    day = models.DateField()

    def __str__(self):
        return self.active