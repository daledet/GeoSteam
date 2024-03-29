from django.db import models
from . import calculations
from iapws import IAPWS97



class Operator(models.Model):
    operator_name = models.CharField(max_length=255, null=True)
    operator_location = models.CharField(max_length=255, null=True)
    operator_contact = models.CharField(max_length=255, null=True)
    operator_email = models.EmailField(max_length=255, null=True)
    operator_phone = models.CharField(max_length=20, null=True, blank=True)    

    def __str__(self):
        return self.operator_name
    
class Well(models.Model):
    operator = models.ForeignKey(Operator, max_length=255, null=True, on_delete=models.CASCADE)
    well_name = models.CharField(max_length=255, null=True)
    well_location = models.CharField(max_length=255, null=True)
    date_time = models.DateTimeField(auto_now=True)
    well_section = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    well_depth = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    well_temperature = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    well_activity = models.CharField(max_length=5000, null=True)

    def __str__(self):
        return self.well_name

class Region(models.Model):
    region_name = models.CharField(max_length=255, null=True)
    region_country = models.CharField(max_length=255, null=True)
    region_contact = models.CharField(max_length=255, null=True)
    region_contact_email = models.CharField(max_length=255, null=True)
    region_contact_phone = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.region_name
    
class Surface(models.Model):
    wellhead_name = models.CharField(max_length=255, null=True)
    temp_bottom_hole  = models.FloatField(max_length=255, null=True) 
    pressure_bottom_hole = models.FloatField(max_length=255, null=True)
    pressure_seperator = models.FloatField(max_length=255, null=True)
    pressure_condensor = models.FloatField(max_length=255, null=True)
    turbine_efficiency = models.FloatField(max_length=255, null=True)
    turbine_exit_pressure = models.FloatField(max_length=255, null=True)
    required_output = models.FloatField(max_length=255, null=True)

    def __str__(self):
        return self.wellhead_name
    
    @property
    def flow_required(self):
        return 100