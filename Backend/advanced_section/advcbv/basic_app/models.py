from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse

# Create your models here.
class School(models.Model):
    name = models.CharField(max_length=256)
    principal = models.CharField(max_length=256)
    location = models.CharField(max_length=256)
    
    def __str__(self) -> str:
        return self.name
    
    def get_absolute_url(self):
        return reverse("basic_app:detail", kwargs={"pk": self.pk})
    
    
class Student(models.Model):
    name = models.CharField(max_length=256)
    age = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
    school = models.ForeignKey(School,
                               related_name='students',
                               on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.name