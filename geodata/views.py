from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import Surface, Region, Well, Operator

def update_wells(request):
  return render(request, 'update_wells.html')

def start(request):
  return render(request, 'start.html')


def wells(request): 
  return render(request, 'wells.html')


def operators(request):
  return render(request, 'operators.html')


def regions(request):
  return render(request, 'regions.html')

def surface(request):
  return render(request, 'surface.html')


def register(request):
  return render(request, 'register.html')

