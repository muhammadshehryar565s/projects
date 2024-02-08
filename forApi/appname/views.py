from django.http import HttpResponse
from rest_framework import viewsets
from appname.models import Company,Employee,Ouruser
from appname.serializers import UserSerializer,EmployeeSerializer,OuruserSerializer,loginSerializer
from rest_framework.mixins import CreateModelMixin
from rest_framework.viewsets import ModelViewSet, GenericViewSet

def home(request):
    return HttpResponse("Welcome to the app's home page!<<<<<<")
class companyViewSet(viewsets.ModelViewSet):
    queryset=Company.objects.all()
    serializer_class=UserSerializer

class employeeViewSet(viewsets.ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer  

# class ouruserViewSet(viewsets.ModelViewSet):
#     queryset=Ouruser.objects.all()
#     serializer_class=OuruserSerializer      

class ouruserViewSet(CreateModelMixin, GenericViewSet):
    queryset = Ouruser.objects.all()
    serializer_class = OuruserSerializer  

class loginViewSet(viewsets.ModelViewSet):
    queryset=Ouruser.objects.all()
    serializer_class=loginSerializer 
