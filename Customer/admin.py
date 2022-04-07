from django.contrib import admin

# Register your models here.
from .models import Customer, CustomerPredictionDataSet

admin.site.register(Customer)
admin.site.register(CustomerPredictionDataSet)
