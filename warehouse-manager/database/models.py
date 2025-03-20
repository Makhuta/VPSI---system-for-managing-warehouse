from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Supplier(models.Model):
    #sid
    name = models.CharField(max_length=50, verbose_name=_('supplier.name'))
    contact = models.CharField(max_length=50, verbose_name=_('supplier.contact'))
    phone = models.CharField(max_length=13, verbose_name=_('supplier.phone'))
    address = models.CharField(max_length=50, verbose_name=_('supplier.address'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('supplier.created_at'))

    def __str__(self):
        return self.name


class Item(models.Model):
    ITEM_STATUS = [
        ('active', _('item.active')),
        ('inactive', _('item.inactive'))
    ]   
    
    # iid
    name = models.CharField(max_length=50, verbose_name=_('item.name'))
    category = models.CharField(max_length=50, verbose_name=_('item.category'))
    price = models.DecimalField(decimal_places=2,max_digits=6, verbose_name=_('item.price'))
    supplier = models.ForeignKey(Supplier,on_delete=models.SET_NULL,null=True, verbose_name=_('item.supplier'))
    status = models.CharField(max_length=10, choices=ITEM_STATUS, default='active', verbose_name=_('item.status'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('item.created_at'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('item.updated_at'))

    def __str__(self):
        return self.name

class Order(models.Model):
    ORDER_STATUS = [
        ('pending', _('order.pending')),
        ('approved', _('order.approved')),
        ('delivered', _('order.delivered')),
        ('canceled', _('order.canceled'))
    ]
    
    # oid
    item = models.ForeignKey(Item,on_delete=models.SET_NULL,null=True, verbose_name=_('order.item'))
    order_date = models.DateTimeField(auto_now_add=True, verbose_name=_('order.order_date'))
    quantity = models.IntegerField(verbose_name=_('order.quantity'))
    status = models.CharField(max_length=10, choices=ORDER_STATUS, default='pending', verbose_name=_('order.status'))
    

class Warehouse(models.Model):
    #wid
    name = models.CharField(max_length=50, verbose_name=_('warehouse.name'))
    location = models.CharField(max_length=50, verbose_name=_('warehouse.location'))

    def __str__(self):
        return self.name

class Stocks(models.Model):
    #sid
    item = models.ForeignKey(Item, on_delete=models.SET_NULL, null=True, verbose_name=_('stock.item'))
    warehouse = models.ForeignKey(Warehouse, on_delete=models.SET_NULL,null=True, verbose_name=_('stock.warehouse'))
    quantity = models.IntegerField(default=0, verbose_name=_('stock.quantity'))
    min_quantity = models.IntegerField(verbose_name=_('stock.min_quantity')) 

    def __str__(self):
        return f'{self.item.name}: {self.warehouse.name}'
