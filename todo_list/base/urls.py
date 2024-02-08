from django.urls import path
from .views import Tasklist
from .views import detailtask
from .views import taskcreate
from .views import updatetask
from.views import customloginview
from.views import deletetask
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/',customloginview.as_view(),name='login'),
    path("logout/",LogoutView.as_view(next_page='login'), name="logout"),
    path("",Tasklist.as_view() ,name="task1"),
    path('task/<int:pk>/', detailtask.as_view() , name='task'),
    path("create",taskcreate.as_view() ,name="create"),
    path("update/<int:pk>/",updatetask.as_view() ,name="update"),
    path("delete/<int:pk>/",deletetask.as_view() ,name="delete"),

]
