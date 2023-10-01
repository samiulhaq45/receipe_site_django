from django.db import models

# Create your models here.
class Products(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=50)
    product_desc = models.CharField(max_length=2000)
    product_img = models.ImageField()

class Student(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    department = models.CharField(max_length=20)
    address = models.CharField(max_length=50)
