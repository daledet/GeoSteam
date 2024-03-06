from django.contrib import admin
from .models import  Operator, Well, Region, Surface

# Register your models here.

admin.site.register(Operator)
admin.site.register(Well)
admin.site.register(Region)
admin.site.register(Surface)

