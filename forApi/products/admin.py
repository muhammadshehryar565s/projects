from django.contrib import admin

# Register your models here.
from .models import Catagory,product,ForCart

admin.site.register(Catagory)
admin.site.register(product)
admin.site.register(ForCart)



