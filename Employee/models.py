from django.db import models

# Create your models here.

class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(null=True, blank=True, max_length=50)
    email = models.EmailField(null=True, blank=True, max_length=50)
    contact = models.IntegerField(null=True, blank=True)
    address = models.CharField(null=True, blank=True, max_length=100)
    image = models.ImageField(null=True, blank=True, upload_to="profiles/", default="profiles/user-default.png")
    salary = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.name

class PredictionDataSet(models.Model):
    id = models.OneToOneField(Employee, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(null=True, blank=True, max_length=50)
    satisfaction_level = models.FloatField(null=True, blank=True)
    last_evaluation = models.FloatField(null=True, blank=True)
    salary = models.CharField(null=True, blank=True, max_length=50)
    department = models.CharField(null=True, blank=True, max_length=50)
    number_project = models.IntegerField(null=True, blank=True)
    average_montly_hours = models.IntegerField(null=True, blank=True)
    time_spend_company = models.IntegerField(null=True, blank=True)
    Work_accident = models.IntegerField(null=True, blank=True)
    promotion_last_5years = models.IntegerField(null=True, blank=True)
    prediction = models.CharField(null=True, blank=True, max_length=50)

    def __str__(self):
        return self.id.name


