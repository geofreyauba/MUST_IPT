from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=14)
    email=models.CharField(max_length=14)
    password=models.CharField(max_length=14)

    def __str__(self):
        return self.name