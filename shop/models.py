from pyexpat import model
import uuid
from django.db import models
import datetime
import time

from django.forms import DateField

class Product(models.Model): 
    Prod_Id = models.UUIDField(primary_key=True, default=uuid.uuid4,editable=False)
    Product_Name = models.CharField(max_length=50,default="")
    Discription = models.TextField()
    Publish_Data = models.DateField()
    Catagory = models.CharField(max_length=50,default="")
    Sub_Catagory = models.CharField(max_length=50,default="")
    Price = models.IntegerField(default=0)
    Image = models.ImageField(default="",upload_to = "shop/images")

    def __str__(self) -> str:
        return self.Product_Name

class Contact(models.Model):
    Contact_ID = models.UUIDField(primary_key=True, default=uuid.uuid4,editable=False)
    Name = models.CharField(max_length=50, default="user")
    Email = models.EmailField(max_length=254)
    Discription = models.TextField()
    Time_Created = models.TimeField(auto_now=True)
    Date_Created = models.DateField(auto_now=True)

    def __str__(self) -> str:
        temp = str(self.Contact_ID)+" "+str("(")+str(self.Time_Created)+str(" ")+str(self.Date_Created)+str(")")
        return temp

class Order(models.Model):
    Order_ID = models.UUIDField(primary_key=True, default=uuid.uuid4,editable=False)
    Name = models.CharField(max_length=50,default='')
    Email = models.EmailField()
    Country = models.CharField(max_length=50,default='')
    Address = models.TextField()
    City = models.CharField(max_length=50,default='')
    State = models.CharField(max_length=50,default='')
    Zip = models.IntegerField()
    Json_Data = models.TextField()
    Time_Ordered = models.TimeField(auto_now=True)
    Date_Ordered = models.DateField(auto_now=True)
    Amount = models.BigIntegerField(default=0)

    def __str__(self) -> str:
        return str(self.Order_ID)

ORDER_STATUS = (
    ('Processing','PROCESSING'), # In Procssing
    ('Shipped','SHIPPING'), # In Shipping
    ('In Transit','IN_TRANSIT'), # In Transit
    ('Out For Delivery','OUT_FOR_DELIVERY'), # Out For Delivery
    ('Delivered','DELIVERED'), # Delivered
)

class Tracker(models.Model):
    Tracking_Id = models.ForeignKey(Order,on_delete=models.CASCADE,editable=False)
    Status = models.CharField(choices=ORDER_STATUS,default='Processing',max_length=20)
    Discription = models.TextField(default='In Processing......')

    def __str__(self) -> str:
        return str(self.Tracking_Id)

