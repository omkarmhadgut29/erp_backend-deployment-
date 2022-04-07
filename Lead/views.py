from django.http.response import HttpResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import generics
from .models import Lead
from .serializers import LeadSerializer

class LeadList(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated] 

    queryset = Lead.objects.all()
    serializer_class = LeadSerializer

class AddLead(APIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated] 

    def post(self, request):
        fields = Lead._meta.get_fields()
        validData = True
        for field in fields:
            if field.name != "id" and field.name != "image":
                if request.data[field.name] == '':
                    validData = False
                    break
        if validData:
            serializer = LeadSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'status': 200, 'message': 'Student added', 'data': serializer.data})
            else:
                return Response({'status': 400, 'message': serializer.errors})
        return Response({'status': 400, 'message': 'Student not created'})

class DeleteLead(APIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated] 

    def post(self, request):
        lead = Lead.objects.get(id=request.data['id'])
        lead.delete()
        return Response({'status': 200, 'message': 'Student deleted'})

class UpdateLead(APIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Lead.objects.all()
    serializer_class = LeadSerializer

    def post(self, request, *args, **kwargs):
        lead = Lead.objects.get(id=request.data['id'])
        fields = request.data.keys()
        for field in fields:
            if field != "id":
                setattr(lead, field, request.data[field])
        lead.save()
        return Response({'status': 200, 'message': 'Student updated'})

