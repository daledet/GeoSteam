from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import Surface, Region, Well, Operator

def update_wells(request):
  return render(request, 'update_wells.html')

def start(request):
  return render(request, 'start.html, {}')
  # template = loader.get_template('start.html')
  # return HttpResponse(template.render())

def wells(request):
  template = loader.get_template('wells.html')
  return HttpResponse(template.render())

def operators(request):
  template = loader.get_template('operators.html')
  return HttpResponse(template.render())

def regions(request):
  template = loader.get_template('regions.html')
  return HttpResponse(template.render())

def surface(request):
  template = loader.get_template('surface.html')
  return HttpResponse(template.render())

def register(request):
  template = loader.get_template('register.html')
  return HttpResponse(template.render())
