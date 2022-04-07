from rest_framework import serializers
from .models import Customer, CustomerPredictionDataSet

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('id', 'name', 'email', 'contact', 'address', 'image')

class CustomerPredictionDataSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerPredictionDataSet
        fields = ('id', 'name','gender','SeniorCitizen','Partner','Dependents','tenure','PhoneService','MultipleLines','InternetService','OnlineSecurity','OnlineBackup','DeviceProtection','TechSupport','StreamingTV','StreamingMovies','Contract','PaperlessBilling','PaymentMethod','MonthlyCharges','TotalCharges','Churn')
