from django import forms
from numpy import save

from blog.models import Fitnessgraph


class Fitnessform(forms.Form):
    active = forms.CharField(max_length = 100, label="active")

    time = forms.IntegerField(label="time")
    day = forms.DateField(label="day")
    
    def save(self):
        data = self.cleaned_data
        post = Fitnessgraph(active = data['active'], time = data['time'], day=data['day'])
        post.save()

