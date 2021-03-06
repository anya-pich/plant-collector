from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('plants/', views.plants_index, name='plants'),
  path('plants/<int:plant_id>/', views.plants_detail, name='detail'),
  path('plants/<int:plant_id>/add_watering/', views.add_watering, name='add_watering'),
]