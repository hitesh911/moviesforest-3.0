from django.db import models


# Create your models here.
class Contact(models.Model):
    sno = models.AutoField(primary_key= True)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=100)
    number = models.CharField(max_length=15)
    content = models.TextField()
    timestamp = models.DateTimeField( blank = True, auto_now_add=True)
    

    def __str__(self):
        return " " + self.name
class Login(models.Model):
    uno = models.AutoField(primary_key= True)
    username = models.CharField( max_length=50)
    username = models.CharField( max_length=50)
    