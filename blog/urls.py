from django.urls import path
from . import views

urlpatterns = [
    path('Fitnessform', views.Fitnessform.as_view(), name='Fitnessform'),
    path('', views.Fitnessgraph.as_view(), name='Fitnessgraph'),
]