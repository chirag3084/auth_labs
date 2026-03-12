from django.db import models

# Create your models here.

class RegisterUser(models.Model):
    FullName = models.CharField(max_length=100)
    DateOfBirth = models.DateField()
    Gender = models.CharField(max_length=10)
    Email = models.EmailField(unique=True)
    PhoneNumber = models.IntegerField()
    Address = models.TextField(default='Varansi, India')
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username
    
