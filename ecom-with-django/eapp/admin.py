from django.contrib import admin

from .models import product,Customer,Cart
# Register your models here

admin.site.register(product)

admin.site.register(Customer)

admin.site.register(Cart)


