from django.db import models

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    about = models.TextField()
    type = models.CharField(max_length=100, choices=(('IT','IT'),('Non IT','Non IT')))
    added_date=models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

class Employe(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    about = models.TextField()
    position = models.CharField(max_length=100,choices=(('Manager','manager'),('Software Developer','SD'),('Team Leader','TL')))

