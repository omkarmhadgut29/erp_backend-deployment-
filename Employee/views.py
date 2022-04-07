from tokenize import String
from django.http.response import HttpResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import generics


# models and serializers
from .models import Employee, PredictionDataSet
from .serializers import EmployeeSerializer, PredictionDataSetSerializer

import joblib
import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Create your views here.

def index(request):
    employees = Employee.objects.all()

    # employee_model = pickle.load(open('employee_model.pkl', 'rb'))
    # employee_model = pd.read_pickle('./employee_model.pkl')
    employee_model = joblib.load('./ML/Employee/employee_model.sav')
    Catagory=['Employee will stay','Employee will Leave']

    # print(EmployeePrediction(request))
    # DataPreprocessing()

    context = {
        'employees': employees,
        # 'prediction': Catagory[int(employee_model.predict(request.POST))]
        'prediction': Catagory[int(employee_model.predict([[1,500,3,6,0,0.90,0.89,1,8]]))]
    }

    return render(request, 'Employee/index.html', context)

def DataPreprocessing(data):
    df = data.copy()

    df.pop("id")
    if df['salary'] == "low":
        df['salary'] = 2
    elif df['salary'] == "medium":
        df['salary'] = 1
    elif df['salary'] == "high":
        df['salary'] = 0


    if df['department'] == "sales":
        df['department'] = 7

    elif df['department'] == "support":
        df['department'] = 8

    elif df['department'] == "accounting":
        df['department'] = 2

    elif df['department'] == "hr":
        df['department'] = 3

    elif df['department'] == "technical":
        df['department'] = 9

    elif df['department'] == "management":
        df['department'] = 4

    elif df['department'] == "IT":
        df['department'] = 0

    elif df['department'] == "product_mng":
        df['department'] = 6

    elif df['department'] == "technical":
        df['department'] = 5

    elif df['department'] == "technical":
        df['department'] = 1

    return df

class EmployeeList(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated] 

    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class AddEmployee(APIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated] 

    def post(self, request):
        fields = list(Employee._meta.get_fields())
        del fields[0:1]
        validData = True

        for field in fields:
            field = str(field).split(".")
            del field[0:2]
            if field[0] != "id" and field[0] != "image":
                if request.data[field[0]] == '':
                    validData = False
                    break
        if validData:
            serializer = EmployeeSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'status': 200, 'message': 'Student added', 'data': serializer.data})
            else:
                return Response({'status': 400, 'message': serializer.errors})
        return Response({'status': 400, 'message': 'Student not created'})

class DeleteEmployee(APIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated] 

    def post(self, request):
        employee = Employee.objects.get(id=request.data['id'])
        employee.delete()
        return Response({'status': 200, 'message': 'Student deleted'})

class UpdateEmployee(APIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def post(self, request, *args, **kwargs):
        employee = Employee.objects.get(id=request.data['id'])
        fields = request.data.keys()
        for field in fields:
            if field != "id":
                setattr(employee, field, request.data[field])
        employee.save()
        return Response({'status': 200, 'message': 'Student updated'})


# Adding PredictionDataSet
class AddPredictionDataSet(APIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated] 

    def post(self, request):

        data = request.data
        Preprocessed_df = DataPreprocessing(data)

        employee_model = joblib.load('./ML/Employee/employee_model.sav')
        Catagory=['Employee will stay','Employee will Leave']

        result = employee_model.predict([list(Preprocessed_df.values())])
        print(result)

        request.data['prediction'] = Catagory[int(result)]
        request.data['name'] = Employee.objects.get(id=request.data['id']).name

        serializer = PredictionDataSetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 200, 'message': 'Prediction Dataset added Successfully.', 'data': serializer.data})
        else:
            return Response({'status': 400, 'message': serializer.errors})
        # return Response({'status': 400, 'message': 'Prediction Dataset added Successfully.', 'data': ''})


# Listing PredictionDataSet
class PredictionDataSetList(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated] 

    queryset = PredictionDataSet.objects.all()
    serializer_class = PredictionDataSetSerializer


# Deleting PredictionDataSet
class DeletePredictionDataSet(APIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated] 

    def post(self, request):
        prediction_data_set = PredictionDataSet.objects.all()
        prediction_data_set.delete()
        return Response({'status': 200, 'message': 'Prediction Dataset Deleted Successfully'})
