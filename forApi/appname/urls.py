from django.urls import path,include
from . import views
from appname.views import companyViewSet,employeeViewSet,ouruserViewSet,loginViewSet
from rest_framework import routers

router=routers.DefaultRouter()
router.register(r'companies',companyViewSet)
router.register(r'employees', employeeViewSet)
router.register(r'ourusers', ouruserViewSet)
router.register(r'loginuser', loginViewSet)


urlpatterns = [
    path('', views.home, name='home'),
    path("api/v1/",include(router.urls))
  
]

