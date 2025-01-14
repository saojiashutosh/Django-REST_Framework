from django.db import models

# Create your models here.
class Customer(models.Model):
    cust_id = models.AutoField(primary_key= True ,auto_created= True )
    cust_name = models.CharField("Customer Name :",max_length=50)
    cust_addr = models.TextField("Customer Address :")
    cust_contact = models.BigIntegerField("Customer Contact :")