from django.db import models
from django.contrib.auth.models import User

# Create your models here.

CATEGORY_CHOICES=(
    ('CR','Curd'),
    ('ML','Milk'),
    ('LS','Lassi'),
    ('MS','Milikshake'),
    ('PN','Paneer'),
    ('CZ','Cheese'),
    ('IC','Ice-Cream'),
)

STATE_CHOICE=(
    ('P','punjab'),
    ('S','sindh'),
    ('K','KPK'),
    ('B','balochistan'),
)



class product(models.Model):
    
    title=models.CharField(max_length=100)
    selling_price=models.FloatField(max_length=200)
    discount_price=models.FloatField(max_length=200)
    composition = models.TextField()
    discription=models.TextField()
    prodapp=models.TextField()
    category=models.CharField(choices=CATEGORY_CHOICES ,max_length=200)
    product_image=models.ImageField(upload_to='product')

    def __str__(self):
        return self.title
    



class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name=models.CharField(max_length=200)
    locality=models.CharField(max_length=200)
    city=models.CharField(max_length=200)
    mobile=models.IntegerField()
    zipcode=models.IntegerField()
    state=models.CharField(choices=STATE_CHOICE,max_length=100)

    def __str__(self):
        return self.name

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product2=models.ForeignKey(product,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)

    @property
    def total_cost(self):
        
        return self.quantity * self.product2.discount_price
    
    