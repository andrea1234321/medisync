from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Medication

# Define the home view
def home(request):
  return render(request, 'home.html')

class MedicationCreate(CreateView):
  model= Medication
  fields= '__all__'
  success_url = '/'
