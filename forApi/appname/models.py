from django.db import models

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    founded_date = models.DateField()
    location = models.CharField(max_length=100)
   

    def __str__(self):
        return self.name

class Employee(models.Model):
    name = models.CharField(max_length=50)
    
    email = models.EmailField()
    
    department = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    company=models.ForeignKey(Company,on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class Ouruser(models.Model):
    name = models.CharField(max_length=50)
    
    email = models.EmailField()
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.name



    
