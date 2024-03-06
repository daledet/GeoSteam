from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def start(request):
  template = loader.get_template('start.html')
  return HttpResponse(template.render())

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