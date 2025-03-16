from django.db import models

# Create your models here.

class Supplier(models.Model):
    #sid
    name = models.CharField(max_length=50)
    contact = models.CharField(max_length=50)
    phone = models.CharField(max_length=13)
    address = models.CharField(max_length=50)
    created_at = models.DateTimeField()

    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    price = models.DecimalField()
    supplier = models.ForeignKey(Supplier,on_delete=models.SET_NULL,null=True)
    #status
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    def __str__(self):
        return self.name

class Order(models.Model):
    # oid
    item = models.ForeignKey(Item,on_delete=models.SET_NULL,null=True)
    order_date = models.DateTimeField()
    quantity = models.IntegerField()
    # status

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
    quanitity = models.IntegerField()
    min_quantity = models.IntegerField()

    def __str__(self):
        res = ''
        res += str(self.item.name)
        res += ": "
        res += str(self.warehouse.name)
        return res
