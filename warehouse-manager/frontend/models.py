from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    price = models.DecimalField()
    #suplier
    #status
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    def __str__(self):
        return self.name

class Order(models.Model):
    # oid
    # iid
    order_date = models.DateTimeField()
    quantity = models.IntegerField()
    # status

class Supplier(models.Model):
    #sid
    name = models.CharField(max_length=50)
    contact = models.CharField(max_length=50)
    phone = models.CharField(max_length=13)
    address = models.CharField(max_length=50)
    created_at = models.DateTimeField()

class Warehouse(models.Model):
    #wid
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)

class Stocks(models.Model):
    #sid
    #iid
    #wid
    quanitity = models.IntegerField()
    min_quantity = models.IntegerField()
