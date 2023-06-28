from django.db import models


# Create your models here.
time_choices = [
  ("QD", "daily (QD)"),
  ("BID", "twice a day (BID)"),
  ("TID", "three times a day (TID)"),
  ("QID", "four times a day (QID)"),
  ("PRN", "as needed (PRN)"),
  ("QHS", "at bedtiitme (QHS)"),
]

# class DayChoices(models.Model):
#   ('Daily', 'Daily'),
#   ('Mon', 'Monday'),
#   ('Tue', 'Tuesday'),
#   ('Wed', 'Wednesday'),
#   ('Thu', 'Thursday'),
#   ('Fri', 'Friday'),
#   ('Sat', 'Saturday'),
#   ('Sun', 'Sunday'),

  
class Medication(models.Model):
  name= models.CharField(max_length=40)
  dose= models.DecimalField(decimal_places=2, max_digits=7)
  unitOfMeasurement= models.CharField(max_length=10)
  time= models.CharField(max_length=3, choices=time_choices)
  # day= models.ManyToManyField(DayChoices)
  reason= models.CharField(max_length=30)
  notes= models.TextField(max_length= 250, blank=True)
  
  def __str__(self): 
    return self.name
