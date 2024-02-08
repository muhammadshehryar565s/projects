from django.db import models

# Create your models here.
class getimage(models.Model):
    image=models.ImageField(upload_to="my_file")
    date=models.DateField(auto_now_add=True)