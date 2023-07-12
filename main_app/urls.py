from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('medications/', views.index, name='index'),
  path('medications/create/', views.MedicationCreate.as_view(), name='medication-create')
]