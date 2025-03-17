from django.db import models

# Create your models here.

class Supplier(models.Model):
    #sid
    name = models.CharField(max_length=50)
    contact = models.CharField(max_length=50)
    phone = models.CharField(max_length=13)
    address = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Item(models.Model):
    ITEM_STATUS = [
        ('active', 'Active'),
        ('inactive', 'Inactive')
    ]   
    
    # iid
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    price = models.DecimalField(decimal_places=2,max_digits=6)
    supplier = models.ForeignKey(Supplier,on_delete=models.SET_NULL,null=True)
    status = models.CharField(max_length=10, choices=ITEM_STATUS, default='active')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    ORDER_STATUS = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('delivered', 'Delivered'),
        ('canceled', 'Canceled')
    ]
    
    # oid
    item = models.ForeignKey(Item,on_delete=models.SET_NULL,null=True)
    order_date = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField()
    status = models.CharField(max_length=10, choices=ORDER_STATUS, default='pending')
    

class Warehouse(models.Model):
    #wid
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Stocks(models.Model):
    #sid
    item = models.ForeignKey(Item, on_delete=models.SET_NULL, null=True)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.SET_NULL,null=True)
    quantity = models.IntegerField(default=0)
    min_quantity = models.IntegerField() 

    def __str__(self):
        return f'{self.item.name}: {self.warehouse.name}'
