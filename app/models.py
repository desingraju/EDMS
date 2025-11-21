from django.db import models

# Create your models here.
class Employee(models.Model):
    First_name=models.CharField(max_length=100)
    Last_name=models.CharField(max_length=100)
    Photo=models.CharField(max_length=100)
    Designation=models.CharField(max_length=100)
    Email_address=models.CharField(max_length=100)
    Phone_number=models.CharField(max_length=100)