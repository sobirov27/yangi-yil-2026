from django.db import models
# Create your models here.
from django.contrib.auth.models import User


class Maktab(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    students_number = models.IntegerField(default=200)
    opened_time = models.DateField()
    created_at = models.DateField()


    def __str__(self):
        return self.name
    

class Director(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    salary = models.DecimalField(max_digits=10,decimal_places=2)
    time_to_work = models.DateField()
    created_at = models.DateField()


    def __str__(self):
        return self.user
    

class Oqituvchi(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    age = models.IntegerField(default=100)
    monthly_salary = models.IntegerField()
    about_teacher = models.TextField(max_length=200)
    time_to_work = models.DateField()
    number_st = models.IntegerField()
    created_at = models.DateField()
    changed_time = models.DateField()

    def __str__(self):
        return self.user
    