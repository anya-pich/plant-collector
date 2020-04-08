from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
  return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')

def about(request):
  return render(request, 'about.html')

def plants_index(request):
  return render(request, 'plants/index.html', {'plants': plants})

class Plant:
  def __init__(self, name, taxonomy, indoor, outdoor, sun, temperature_f, purchase_date, diameter_i, photo, watering_frequency):
      self.name = name
      self.taxonomy = taxonomy
      self.indoor = indoor
      self.outdoor = outdoor
      self.sun = sun
      self.temperature_f = temperature_f
      self.purchase_date = purchase_date
      self.diameter_i = diameter_i
      self.photo = photo
      self.watering_frequency = watering_frequency

plants = [
  Plant('Cactus', 'Cactaceae Mammilaria', True, False, 'SU', 54, 'Feb 2020', 4, 'photo', 'every week'),
  Plant('Succulent', 'Succulent Crassula', True, False, 'SU', 54, 'Feb 2020', 4, 'photo', 'every week'),
  Plant('Bushy thing', 'TBD', True, False, 'SU', 54, 'Feb 2020', 4, 'photo', 'every week'),
]
