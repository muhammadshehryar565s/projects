

from rest_framework import routers, serializers, viewsets
from appname.models import Company,Employee,Ouruser

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Company
        fields = "__all__"

        
class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
      
    class Meta:
        model=Employee
        fields="__all__"

class OuruserSerializer(serializers.HyperlinkedModelSerializer):
      
    class Meta:
        model=Ouruser
        fields= ['name','email','password']        

      
class loginSerializer(serializers.HyperlinkedModelSerializer):
      
    class Meta:
        model=Ouruser
        fields= ['email','password']                    