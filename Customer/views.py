from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import generics

from .models import Customer, CustomerPredictionDataSet
from .serializers import CustomerSerializer, CustomerPredictionDataSetSerializer

import joblib



class CustomerList(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated] 

    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class AddCustomer(APIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated] 

    def post(self, request):
        fields = list(Customer._meta.get_fields())
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
            serializer = CustomerSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'status': 200, 'message': 'Student added', 'data': serializer.data})
            else:
                return Response({'status': 400, 'message': serializer.errors})
        return Response({'status': 400, 'message': 'Student not created'})

class DeleteCustomer(APIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated] 

    def post(self, request):
        customer = Customer.objects.get(id=request.data['id'])
        customer.delete()
        return Response({'status': 200, 'message': 'Student deleted'})

class UpdateCustomer(APIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def post(self, request, *args, **kwargs):
        customer = Customer.objects.get(id=request.data['id'])
        fields = request.data.keys()
        for field in fields:
            if field != "id":
                setattr(customer, field, request.data[field])
        customer.save()
        return Response({'status': 200, 'message': 'Student updated'})

def DataPreprocessing(data):
    df = data.copy()

    df.pop("id")

    dict1 = {
        'gender': {'Female': 0, 'Male': 1}, 
        'Partner': {'Yes': 1, 'No': 0}, 
        'Dependents': {'No': 0, 'Yes': 1}, 
        'PhoneService': {'No': 0, 'Yes': 1}, 
        'MultipleLines': {'No phone service': 1, 'No': 0, 'Yes': 2}, 
        'InternetService': {'DSL': 0, 'Fiber optic': 1, 'No': 2}, 
        'OnlineSecurity': {'No': 0, 'Yes': 2, 'No internet service': 1}, 
        'OnlineBackup': {'Yes': 2, 'No': 0, 'No internet service': 1}, 
        'DeviceProtection': {'No': 0, 'Yes': 2, 'No internet service': 1}, 
        'TechSupport': {'No': 0, 'Yes': 2, 'No internet service': 1}, 
        'StreamingTV': {'No': 0, 'Yes': 2, 'No internet service': 1}, 
        'StreamingMovies': {'No': 0, 'Yes': 2, 'No internet service': 1}, 
        'Contract': {'Month-to-month': 0, 'One year': 1, 'Two year': 2}, 
        'PaperlessBilling': {'Yes': 1, 'No': 0}, 
        'PaymentMethod': {'Electronic check': 2, 'Mailed check': 3, 
        'Bank transfer (automatic)': 0, 'Credit card (automatic)': 1},
        }

    for key in dict1.keys():
        for value in dict1[key].keys():
            # df[key] = dict1[key][value]
            if df[key] == value:
                df[key] = dict1[key][value]
    
    return df

class AddCustomerPredictionDataSet(APIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated] 

    def post(self, request):

        data = request.data
        Preprocessed_df = DataPreprocessing(data)

        customer_model = joblib.load('./ML/Customer/customer_prediction_model.sav')
        Catagory=['Customer will stay','Customer will Leave']

        result = customer_model.predict([list(Preprocessed_df.values())])

        request.data['Churn'] = Catagory[int(result)]

        serializer = CustomerPredictionDataSetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 200, 'message': 'Prediction Dataset added Successfully.', 'data': serializer.data})
        else:
            return Response({'status': 400, 'message': serializer.errors})
        # return Response({'status': 200, 'message': 'Prediction Dataset added Successfully.'})

# Listing PredictionDataSet
class CustomerPredictionDataSetList(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated] 

    queryset = CustomerPredictionDataSet.objects.all()
    serializer_class = CustomerPredictionDataSetSerializer


# Deleting PredictionDataSet
class CustomerDeletePredictionDataSet(APIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated] 

    def post(self, request):
        prediction_data_set = CustomerPredictionDataSet.objects.all()
        prediction_data_set.delete()
        return Response({'status': 200, 'message': 'Prediction Dataset Deleted Successfully'})
