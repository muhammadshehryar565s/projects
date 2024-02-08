from django.shortcuts import render
from django.views import View
from .models import product,Customer,Cart
from django.db.models import Count
from .  forms import CustomRegistrationForm,CustomerProfielForm
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User






# Create your views here.

def index(request):
    return render(request, 'eapp/index.html')

def about(request):
    return render(request, 'eapp/about.html')


def home(request):
    return render (request, 'eapp/home.html')

def address1(request):
    add1 = Customer.objects.filter(user=request.user)
    print(add1)
    return render(request, 'eapp/address.html', {'add1': add1})



class category(View):

    def get(self,request,val):
        products= product.objects.filter(category=val)
        title=product.objects.filter(category=val).values('title')
        return render(request,'eapp/category.html',locals())
    
def showcart(request):
    user=request.user
    cart=Cart.objects.filter(user=user)
    return render(request,'ecom/showcard.html',locals())    
    





class categorytitle(View):
    def get(self, request, val):
        products = product.objects.filter(title=val)
        category = products.first().category if products else None
        title = product.objects.filter(category=category).values('title')
        return render(request, 'eapp/category.html', locals())

class productDetail(View):
    def get(self, request,pk):
         product1=product.objects.get(pk=pk)
         return render(request, 'eapp/product_details.html',locals())
        




class CustomerRegistration(View):
    def get(self, request):
        form1 = CustomRegistrationForm()
        return render(request, 'eapp/RegistratonForm.html', {'form1': form1})

    def post(self, request):
        form1 = CustomRegistrationForm(request.POST)
        if form1.is_valid():
            form1.save()
            messages.success(request, "Congratulations! User registered successfully.")
            return render(request, 'eapp/RegistratonForm.html', {'form1': form1})
           # return redirect('home')  # Replace 'home' with the appropriate URL or view name
        else:
            messages.error(request, "Invalid input data. Please try again.")
            return render(request, 'eapp/RegistratonForm.html', {'form1': form1})
        



class ProfileView(View):
    def get(self, request):
        form = CustomerProfielForm()
        return render(request, 'eapp/profile.html', {'form': form})

    def post(self, request):
        form = CustomerProfielForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Congratulations! User registered successfully.")
            return render(request, 'eapp/profile.html', {'form': form})
        else:
            messages.error(request, "Invalid input data. Please try again.")
            return render(request, 'eapp/profile.html', {'form': form})
        

def add_to_cart(request):
    
     user=request.user
     product_id=request.GET.get('prod_id')
     product=product.objects.get(id=product_id)
     Cart(user=user,product=product)
     return redirect('/cart')

def showcart(request):
    user=request.user
    cart=Cart.objects.filter(user=user)
    return render(request,'eapp/showcard.html')

            
        







# class CustomPasswordResetView(PasswordResetView):
#     form_class = passwordchange
#     template_name = 'eapp/password_reset.html'
#     # success_url = '/password_reset/'  # Specify the URL to redirect to after successful password reset

#     def get_form_kwargs(self):
#         kwargs = super().get_form_kwargs()
#         kwargs['user'] = self.request.user  # Pass the user object to the form
#         return kwargs

#     def get(self, request, *args, **kwargs):
#         # Redirect authenticated users to a different view
#         if self.request.user.is_authenticated:
#             # return redirect('password_reset')  # Replace 'home' with the appropriate URL or view name
#             return super().get(request, *args, **kwargs)
        

# def emailpassword(request):
#     form=emailpassword()
#     return render(request,'eapp/emailpassword.html',locals())



# class emailpassword(View):
#     def get( request):
#         form = emailpassword()
#         return render(request, 'eapp/emailpassword.html', {'form': form})
#     def post(self, request):
#         form = emailpassword(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, "Congratulations! User registered successfully.")
#             return render(request, 'eapp/emailpassword.html', {'form': form})
#             # return redirect('home')  # Replace 'home' with the appropriate URL or view name
#         else:
#             messages.error(request, "Invalid input data. Please try again.")
#             return render(request, 'eapp/emailpassword.html', {'form': form})




       

                    
