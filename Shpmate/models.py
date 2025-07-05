from django.db import models

# Create your models here.
class login(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    usertype = models.CharField(max_length=100)

class User(models.Model):
    Uname = models.CharField(max_length=100)
    Email = models.CharField(max_length=100)
    Phone = models.CharField(max_length=100)
    Place = models.CharField(max_length=100)
    post = models.CharField(max_length=100)
    pin = models.CharField(max_length=100)
    Dob = models.CharField(max_length=100)
    Image = models.CharField(max_length=250)
    LOGIN = models.ForeignKey(login,on_delete=models.CASCADE,default=1)

class Shop(models.Model):
    Sname =  models.CharField(max_length=100)
    Email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    lattitude = models.CharField(max_length=100)
    lognitude = models.CharField(max_length=100)
    Ownername = models.CharField(max_length=100)
    Place = models.CharField(max_length=100)
    Image = models.CharField(max_length=250)
    LOGIN = models.ForeignKey(login,on_delete=models.CASCADE,default=1)

class Complaints(models.Model):
    date = models.CharField(max_length=100)
    complaints = models.CharField(max_length=100)
    replay = models.CharField(max_length=100)
    replay_date = models.CharField(max_length=100)
    USER = models.ForeignKey(User,on_delete=models.CASCADE,default=1)

class feedback(models.Model):
    date = models.CharField(max_length=100)
    feedback = models.CharField(max_length=100)
    USER = models.ForeignKey(User,on_delete=models.CASCADE,default=1)

class categorey(models.Model):
    Name = models.CharField(max_length=100)

class Product(models.Model):
    Pname = models.CharField(max_length=100)
    Purchase_date =  models.CharField(max_length=100)
    Man_date = models.CharField(max_length=100)
    Price = models.CharField(max_length=100)
    Stock = models.CharField(max_length=100)
    Image = models.CharField(max_length=200)
    CATEGOREY = models.ForeignKey(categorey,on_delete=models.CASCADE,default=1)
    SHOP = models.ForeignKey(Shop,on_delete=models.CASCADE,default=1)

class Order(models.Model):
    date = models.CharField(max_length=100)
    Amount = models.CharField(max_length=100)
    Status = models.CharField(max_length=100)
    payment_date = models.CharField(max_length=100)
    payment_status = models.CharField(max_length=100)
    payment_method = models.CharField(max_length=100)
    SHOP = models.ForeignKey(Shop,on_delete=models.CASCADE,default=1)
    USER = models.ForeignKey(User,on_delete=models.CASCADE,default=1)

class Order_sub(models.Model):
    Quantity = models.CharField(max_length=100)
    PRODUCT = models.ForeignKey(Product,on_delete=models.CASCADE,default=1)
    ORDER = models.ForeignKey(Order,on_delete=models.CASCADE,default=1)

class Review(models.Model):
    date = models.CharField(max_length=100)
    Review = models.CharField(max_length=100)
    Ratings = models.CharField(max_length=100)
    USER = models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    SHOP = models.ForeignKey(Shop,on_delete=models.CASCADE,default=1)

class cart(models.Model):
    Quantity = models.CharField(max_length=100)
    PRODUCT = models.ForeignKey(Product,on_delete=models.CASCADE,default=1)
    USER = models.ForeignKey(User,on_delete=models.CASCADE,default=1)










