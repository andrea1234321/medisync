from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('medications/', views.index, name='index'),
  path('medications/<int:pk>/', views.MedicationDetail.as_view(), name='medication-detail'),
  path('medications/create/', views.MedicationCreate.as_view(), name='medication-create'),
  path('medications/<int:pk>/update/', views.MedicationUpdate.as_view(), name='medication-update'),
]