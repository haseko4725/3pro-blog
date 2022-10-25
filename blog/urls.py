from django.urls import path
from . import views

urlpatterns = [
    #path('',views.Fitnessform, name='Fitnessform'),
    path('', views.Fitnessgraph.as_view(), name='Fitnessgraph'),
]