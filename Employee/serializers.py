from rest_framework import serializers
from .models import Employee, PredictionDataSet

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('id', 'name', 'email', 'contact', 'address', 'image', 'salary')

class PredictionDataSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = PredictionDataSet
        fields = ('id','name', 'prediction', 'satisfaction_level', 'last_evaluation', 'salary', 'department', 'number_project', 'average_montly_hours', 'time_spend_company', 'Work_accident', 'promotion_last_5years')
