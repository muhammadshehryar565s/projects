from django.db import models

# Create your models here.
class Catagory(models.Model):
    name=models.CharField(max_length=100)
    cat_slug=models.SlugField()

    class Meta:
        ordering =('name',)
    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return f'/{self.slug}/'
    

class product(models.Model):
    category = models.ForeignKey(Catagory, related_name='product', on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    pro_slug=models.SlugField()
    description=models.TextField(blank=True,null=True)
    price=models.DecimalField(max_digits=20,decimal_places=2)
    image=models.ImageField(upload_to="uploads/",blank=True,null=True)
    thumnail=models.ImageField(upload_to="uploads/",blank=True,null=True)
    data=models.DateField(auto_now_add=True)

 
    class Meta:
        ordering =('name',)
    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return f'/{self.slug}/'
    


class ForCart(models.Model):
    name=models.CharField(max_length=100)
    price=models.DecimalField(max_digits=20,decimal_places=2)
    # image=models.ImageField(upload_to="uploads/")

    def __str__(self):
        return self.name
    class Meta:
        ordering =('name',)
    # def __str__(self):
    #     return self.name

    # def get_absolute_url(self):
    #     return f'/{self.slug}/'
