from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Plant
from .forms import WateringForm

# Create your views here.
def home(request):
  return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')

def about(request):
  return render(request, 'about.html')

def plants_index(request):
  plants = Plant.objects.all()
  return render(request, 'plants/index.html', {'plants': plants})

def plants_detail(request, plant_id):
  plant = Plant.objects.get(id=plant_id)
  watering_form = WateringForm()
  return render(request, 'plants/detail.html', { 
    'plant': plant, 'watering_form': watering_form 
  })

def add_watering(request, plant_id):
  form = WateringForm(request.POST)
  if form.is_valid():
    new_watering = form.save(commit=False)
    new_watering.plant_id = plant_id
    new_watering.save()
  return redirect('detail', plant_id=plant_id)