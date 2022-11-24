from django.db import models

# Create your models here.
class UserLogin(models.Model):
    name = models.CharField(max_length=64)
    surname = models.CharField(max_length=64)
    email = models.EmailField(max_length=150, unique=True)
    password = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.email