from django.db import models
from datetime import date

# Create your models here.
# class Plant(models.Model):
#   name = models.CharField(max_length=100)
#   taxonomy = models.CharField(max_length=255, blank=True, null=True)
#   indoor = models.BooleanField()
#   outdoor = models.BooleanField()
#   SUN_LEVELS = (
#     ('SU', 'sun'),
#     ('PS', 'part shade'),
#     ('SH', 'shade'),
#   )
#   sun = models.CharField(
#     max_length=2,
#     choices=SUN_LEVELS
#   ) 
#   temperature_f = models.FloatField(blank=True, null=True)
#   purchase_date = models.DateField(blank=True, null=True)
#   diameter_i = models.FloatField(blank=True, null=True)
#   photo = models.ImageField(blank=True, null=True)
#   watering_frequency = models.DurationField()

CAT = (
  ('W', 'Water'),
  ('F', 'Plant food')
)

class Plant(models.Model):
  name = models.CharField(max_length=100)
  description = models.TextField(max_length=255)
  diameter = models.FloatField()
  photo = models.ImageField(blank=True, null=True)
  watering_frequency = models.DurationField()
  def __str__(self):
    return self.name
  def is_watered(self):
    # last_watered = 
    # time_elapsed = date.today() - last_watered
    # self.watering_frequency > time_elapsed
    return date.today() - self.watering_set.latest('date').date < self.watering_frequency

class Watering(models.Model):
  date = models.DateField('watering date')
  cat = models.CharField(
    'watering type',
    max_length=1,
    choices=CAT,
    default=CAT[0][0]
  )
  plant = models.ForeignKey(Plant, on_delete=models.CASCADE)
  def __str__(self):
    return f"{self.get_cat_display()} on {self.date}"
  class Meta:
    ordering = ['-date']