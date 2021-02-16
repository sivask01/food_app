from django.db import models

class Login(models.Model):
    Username= models.CharField(max_length=50)
    password= models.IntegerField()    

    def __str__(self):
        return self.Username

class Customer(models.Model):
    UserId= models.CharField(max_length=50)
    Id= models.IntegerField()
    title=models.CharField(max_length=1000)
    body=models.CharField(max_length=2000)

    def __str__(self):
        return self.UserId

