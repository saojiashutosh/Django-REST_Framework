from django.db import models

# Create your models here.
class Employee(models.Model):
    eno = models.IntegerField("Employee Number")
    ename = models.CharField("Employee Name", max_length=20)
    esal = models.FloatField("Employee Salary")