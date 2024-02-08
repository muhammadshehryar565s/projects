
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView
from .forms import Loginform,mypasswordreset,passwordchange,emailpassword



urlpatterns = [
    
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('CustomerRegistration/', views.CustomerRegistration.as_view(), name='CustomerRegistration'),
    path('category/<slug:val>/', views.category.as_view(), name='category'),
    path('category-title/<slug:val>/', views.categorytitle.as_view(), name='category-title'),
    path('profile/',views.ProfileView.as_view(), name='profile'),
    path('address/',views.address1, name='address'),                       
    path('profile/',views.ProfileView.as_view(), name='profile'),
    path('product_detail/<slug:pk>/', views.productDetail.as_view(), name='product_detail'),
    # path('add-to-cart/',views.add_to_cart,name='add_to_cart'), 
    path('showcart/',views.showcart,name='showcart'),   
    
                                                                                                                                                                                                                            
    
    path('login/', LoginView.as_view(template_name='eapp/login.html',authentication_form=Loginform),name='login'),
    
#     # path('password_reset/', CustomPasswordResetView.as_view(), name='password_reset'),
#     # path('password_resetdone/', LoginView.as_view(template_name='eapp/password_resetdone.html', form_class=mypasswordreset), name='password_resetdone'),

#     path('profile/',views.ProfileView.as_view(), name='profile'),
#     path('address/',views.address1, name='address'),
    
   


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)