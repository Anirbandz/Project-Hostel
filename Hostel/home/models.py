from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.EmailField( max_length=254)
    desc = models.TextField()
    date = models.DateField()

class Meal(models.Model):
    name = models.CharField(max_length=50)
    mealstatus = models.CharField(max_length=50)
    date = models.DateField()

class Application(models.Model):
    f_name = models.CharField(max_length=50)
    l_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    address1 = models.TextField( max_length=254)
    address2 = models.TextField(max_length=254)
    c_number = models.CharField(max_length=50)
    email = models.EmailField( max_length=254)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    zip = models.CharField(max_length=50)
    d_name = models.CharField(max_length=50)
    year = models.CharField(max_length=50)
    reg_number = models.CharField(max_length=50)
    a_date = models.CharField(max_length=50)
    cast = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    distance = models.CharField(max_length=50)
    date = models.DateField()

    def __str__(self):
        return self.name