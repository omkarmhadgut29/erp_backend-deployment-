from django.db import models

# Create your models here.

class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(null=True, blank=True, max_length=50)
    email = models.EmailField(null=True, blank=True, max_length=50)
    contact = models.IntegerField(null=True, blank=True)
    address = models.CharField(null=True, blank=True, max_length=100)
    image = models.ImageField(null=True, blank=True, upload_to="profiles/", default="profiles/user-default.png")

    def __str__(self):
        return self.name

class CustomerPredictionDataSet(models.Model):
    id = models.OneToOneField(Customer, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(null=True, blank=True, max_length=50)
    gender = models.CharField(null=True, blank=True, max_length=50)
    SeniorCitizen = models.IntegerField(null=True, blank=True)
    Partner = models.CharField(null=True, blank=True, max_length=50)
    Dependents = models.CharField(null=True, blank=True, max_length=50)
    tenure = models.IntegerField(null=True, blank=True)
    PhoneService = models.CharField(null=True, blank=True, max_length=50)
    MultipleLines = models.CharField(null=True, blank=True, max_length=50)
    InternetService = models.CharField(null=True, blank=True, max_length=50)
    OnlineSecurity = models.CharField(null=True, blank=True, max_length=50)
    OnlineBackup = models.CharField(null=True, blank=True, max_length=50)
    DeviceProtection = models.CharField(null=True, blank=True, max_length=50)
    TechSupport = models.CharField(null=True, blank=True, max_length=50)
    StreamingTV = models.CharField(null=True, blank=True, max_length=50)
    StreamingMovies = models.CharField(null=True, blank=True, max_length=50)
    Contract = models.CharField(null=True, blank=True, max_length=50)
    PaperlessBilling = models.CharField(null=True, blank=True, max_length=50)
    PaymentMethod = models.CharField(null=True, blank=True, max_length=50)
    MonthlyCharges = models.FloatField(null=True, blank=True)
    TotalCharges = models.FloatField(null=True, blank=True)
    Churn = models.CharField(null=True, blank=True, max_length=50)

    def __str__(self):
        return self.id.name