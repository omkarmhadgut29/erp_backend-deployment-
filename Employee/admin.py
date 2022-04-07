from django.contrib import admin

# Register your models here.
from .models import Employee, PredictionDataSet

admin.site.register(Employee)
admin.site.register(PredictionDataSet)
