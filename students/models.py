from django.db import models

# Create your models here.
from django.db import models

class Student(models.Model):

    prn = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    age = models.IntegerField()
    course = models.CharField(max_length=50)
    percentage = models.FloatField()   # NEW FIELD


    def __str__(self):
        return self.name
