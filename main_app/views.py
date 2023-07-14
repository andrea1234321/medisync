from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic import DetailView
from .models import Medication

# Define the home view
def home(request):
  return render(request, 'home.html')

def index(request):
  medications= Medication.objects.all()
  return render(request, 'medications/index.html', {'medications': medications})

class MedicationCreate(CreateView):
  model= Medication
  fields= '__all__'
  success_url = '/medications'

class MedicationDetail(DetailView):
  queryset= Medication.objects.all()