from django.urls import path
from . import views

urlpatterns = [
    path('', views.start, name='start'),
    path('wells', views.wells, name='wells'),
    path('operators', views.operators, name='operators'),
    path('regions', views.regions, name='regions'),
    path('surface', views.surface, name='surface'),
]