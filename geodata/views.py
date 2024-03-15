from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import Surface, Region, Well, Operator

def home(request):
  return render(request, 'home.html')

def update_wells(request):
  return render(request, 'update_wells.html')

def start(request):
  wells = Well.objects.all()
  return render(request, 'start.html', {'wells': wells})


def wells(request):
  wells = Well.objects.all() 
  return render(request, 'wells.html', {'wells': wells})


def operators(request):
  operators = Operator.objects.all() 
  return render(request, 'operators.html', {'operators': operators})

def regions(request):
  regions = Region.objects.all()
  return render(request, 'regions.html', {'regions': regions})

def surface(request):
  surfaces = Surface.objects.all()
  return render(request, 'surface.html', {'surfaces': surfaces})


def register(request):
  return render(request, 'register.html')

