from django.db import models
from django.contrib.auth.models import AbstractBaseUser

class Account(AbstractBaseUser):
    mobile_number = models.CharField(max_length=10, unique=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    USERNAME_FIELD = 'mobile_number'


class Store(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    link = models.CharField(max_length=100, unique=True)
    owner = models.ForeignKey(Account, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)


class Categories(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)


class Products(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    mrp = models.FloatField(default=0)
    sale_price = models.FloatField(default=0)
    image = models.CharField(max_length=500)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)


class Cart(models.Model):
    customer = models.ForeignKey('Customers', on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    qty = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)


class Orders(models.Model):
    ORDER_CHOICES=((0,'Pending'),(1,'Accepted'))
    customer = models.ForeignKey('Customers', on_delete=models.CASCADE)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    total_price = models.FloatField(default=0)
    status = models.IntegerField(default=0,choices=ORDER_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

class OrderItems(models.Model):
    order = models.ForeignKey(Orders, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    price = models.FloatField(default=0)
    quantity = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

class Customers(models.Model):
    mobile_number = models.CharField(max_length=10, unique=True)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)