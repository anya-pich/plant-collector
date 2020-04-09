from django.db import models

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

class Plant(models.Model):
  name = models.CharField(max_length=100)
  description = models.TextField(max_length=255)
  diameter = models.FloatField()
  photo = models.ImageField(blank=True, null=True)
  watering_frequency = models.DurationField()
  def __str__(self):
    return self.name