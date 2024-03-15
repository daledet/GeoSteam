from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('start', views.start, name='start'),
    path('wells', views.wells, name='wells'),
    path('update_wells', views.update_wells, name='update_wells'),
    path('operators', views.operators, name='operators'),
    path('regions', views.regions, name='regions'),
    path('surface', views.surface, name='surface'),
    path('register', views.register, name='register'),
]