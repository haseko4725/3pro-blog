from django.contrib import admin
from .models import Fitnessgraph
from .forms import Fitnessform

admin.site.register(Fitnessgraph)
admin.site.register(Fitnessform)
