from django.shortcuts import render
from .models import Fitnessgraph
from django.views.generic import ListView
from .forms import Fitnessform


#def Fitnessform(request):
    #form = Fitnessform()
    #return render(request, 'blog/Fitnessform.html', {'form': form})

class Fitnessgraph(ListView):
    queryset = Fitnessgraph.objects.all()
    context_object_name = 'Fitnessgraph'
    template_name = 'Fitnessgraph.html'
    model = Fitnessgraph


