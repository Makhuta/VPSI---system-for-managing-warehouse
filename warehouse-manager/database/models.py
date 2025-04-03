from django.db import models
from django.utils.translation import gettext_lazy as _
import random
from django.conf import settings
from django.contrib.auth.models import User
from currency_converter import CurrencyConverter
import iso4217parse
from django.forms.models import model_to_dict

# Create your models here.

class GeneratingModel(models.Model):
    class Meta:
        abstract = True
    def generate():
        print("Default generate need override.")

class Supplier(GeneratingModel):
    #sid
    name = models.CharField(max_length=50, verbose_name=_('database.supplier.name'))
    contact = models.CharField(max_length=50, verbose_name=_('database.supplier.contact'))
    phone = models.CharField(max_length=13, verbose_name=_('database.supplier.phone'))
    address = models.CharField(max_length=50, verbose_name=_('database.supplier.address'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('database.supplier.created_at'))

    def __str__(self):
        return self.name
    
    def generate():
        FIRST_NAMES = [
            "Emma", "Liam", "Olivia", "Noah", "Ava", "Elijah", "Sophia", "James", "Isabella", "Benjamin",
            "Charlotte", "Lucas", "Mia", "Mason", "Amelia", "Ethan", "Harper", "Alexander", "Evelyn", "Henry",
            "Abigail", "Sebastian", "Ella", "Daniel", "Scarlett"
        ]
        LAST_NAMES = [
            "Johnson", "Smith", "Brown", "Williams", "Jones", "Garcia", "Miller", "Davis", "Rodriguez", "Martinez",
            "Hernandez", "Lopez", "Gonzalez", "Wilson", "Anderson", "Thomas", "Taylor", "Moore", "Jackson", "Martin",
            "Lee", "Perez", "Thompson", "White", "Harris"
        ]
        ADDRESSES = [
            "123 Maple St, Springfield, IL 62704",
            "456 Oak Ave, Columbus, OH 43215",
            "789 Pine Rd, Denver, CO 80203",
            "234 Elm St, Austin, TX 73301",
            "567 Birch Blvd, Seattle, WA 98101",
            "890 Cedar Dr, Miami, FL 33101",
            "345 Walnut St, Atlanta, GA 30301",
            "678 Cherry Ln, Boston, MA 02101",
            "901 Ash Ave, Phoenix, AZ 85001",
            "112 Poplar Ct, Nashville, TN 37201",
            "223 Sycamore St, Detroit, MI 48201",
            "334 Magnolia Rd, Raleigh, NC 27601",
            "445 Willow Blvd, Dallas, TX 75201",
            "556 Cypress Ave, Orlando, FL 32801",
            "667 Spruce Dr, Minneapolis, MN 55401",
            "778 Redwood Ln, Portland, OR 97201",
            "889 Hickory St, Denver, CO 80204",
            "990 Palm Ct, San Diego, CA 92101",
            "1010 Alder Rd, Philadelphia, PA 19101",
            "1111 Fir Ave, Chicago, IL 60601",
            "1212 Bayberry Blvd, Houston, TX 77001",
            "1313 Laurel St, San Francisco, CA 94101",
            "1414 Chestnut Ct, Los Angeles, CA 90001",
            "1515 Juniper Dr, Las Vegas, NV 89101",
            "1616 Dogwood Rd, Charlotte, NC 28201"
        ]
        PHONES = [
            "(217) 555-1234", "(614) 555-5678", "(303) 555-9012", "(512) 555-3456", "(206) 555-7890",
            "(305) 555-2345", "(404) 555-6789", "(617) 555-0123", "(602) 555-4567", "(615) 555-8901",
            "(313) 555-2345", "(919) 555-6789", "(214) 555-0123", "(407) 555-4567", "(612) 555-8901",
            "(503) 555-2345", "(303) 555-6789", "(619) 555-0123", "(215) 555-4567", "(312) 555-8901",
            "(713) 555-2345", "(415) 555-6789", "(213) 555-0123", "(702) 555-4567", "(704) 555-8901"
        ]
        EMAILS = [
            "emma.johnson@email.com", "liam.smith@email.com", "olivia.brown@email.com", "noah.williams@email.com",
            "ava.jones@email.com", "elijah.garcia@email.com", "sophia.miller@email.com", "james.davis@email.com",
            "isabella.rodriguez@email.com", "benjamin.martinez@email.com", "charlotte.hernandez@email.com",
            "lucas.lopez@email.com", "mia.gonzalez@email.com", "mason.wilson@email.com", "amelia.anderson@email.com",
            "ethan.thomas@email.com", "harper.taylor@email.com", "alexander.moore@email.com", "evelyn.jackson@email.com",
            "henry.martin@email.com", "abigail.lee@email.com", "sebastian.perez@email.com", "ella.thompson@email.com",
            "daniel.white@email.com", "scarlett.harris@email.com"
        ]
        generated = Supplier(
            name=f'{random.choice(FIRST_NAMES)} {random.choice(LAST_NAMES)}',
            contact=random.choice(EMAILS),
            phone=random.choice(PHONES),
            address=random.choice(ADDRESSES)
        )
        generated.save()

class Customer(GeneratingModel):
    #sid
    name = models.CharField(max_length=50, verbose_name=_('database.supplier.name'))
    contact = models.CharField(max_length=50, verbose_name=_('database.supplier.contact'))
    phone = models.CharField(max_length=13, verbose_name=_('database.supplier.phone'))
    address = models.CharField(max_length=50, verbose_name=_('database.supplier.address'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('database.supplier.created_at'))

    def __str__(self):
        return self.name
    
    def generate():
        FIRST_NAMES = [
            "Emma", "Liam", "Olivia", "Noah", "Ava", "Elijah", "Sophia", "James", "Isabella", "Benjamin",
            "Charlotte", "Lucas", "Mia", "Mason", "Amelia", "Ethan", "Harper", "Alexander", "Evelyn", "Henry",
            "Abigail", "Sebastian", "Ella", "Daniel", "Scarlett"
        ]
        LAST_NAMES = [
            "Johnson", "Smith", "Brown", "Williams", "Jones", "Garcia", "Miller", "Davis", "Rodriguez", "Martinez",
            "Hernandez", "Lopez", "Gonzalez", "Wilson", "Anderson", "Thomas", "Taylor", "Moore", "Jackson", "Martin",
            "Lee", "Perez", "Thompson", "White", "Harris"
        ]
        ADDRESSES = [
            "123 Maple St, Springfield, IL 62704",
            "456 Oak Ave, Columbus, OH 43215",
            "789 Pine Rd, Denver, CO 80203",
            "234 Elm St, Austin, TX 73301",
            "567 Birch Blvd, Seattle, WA 98101",
            "890 Cedar Dr, Miami, FL 33101",
            "345 Walnut St, Atlanta, GA 30301",
            "678 Cherry Ln, Boston, MA 02101",
            "901 Ash Ave, Phoenix, AZ 85001",
            "112 Poplar Ct, Nashville, TN 37201",
            "223 Sycamore St, Detroit, MI 48201",
            "334 Magnolia Rd, Raleigh, NC 27601",
            "445 Willow Blvd, Dallas, TX 75201",
            "556 Cypress Ave, Orlando, FL 32801",
            "667 Spruce Dr, Minneapolis, MN 55401",
            "778 Redwood Ln, Portland, OR 97201",
            "889 Hickory St, Denver, CO 80204",
            "990 Palm Ct, San Diego, CA 92101",
            "1010 Alder Rd, Philadelphia, PA 19101",
            "1111 Fir Ave, Chicago, IL 60601",
            "1212 Bayberry Blvd, Houston, TX 77001",
            "1313 Laurel St, San Francisco, CA 94101",
            "1414 Chestnut Ct, Los Angeles, CA 90001",
            "1515 Juniper Dr, Las Vegas, NV 89101",
            "1616 Dogwood Rd, Charlotte, NC 28201"
        ]
        PHONES = [
            "(217) 555-1234", "(614) 555-5678", "(303) 555-9012", "(512) 555-3456", "(206) 555-7890",
            "(305) 555-2345", "(404) 555-6789", "(617) 555-0123", "(602) 555-4567", "(615) 555-8901",
            "(313) 555-2345", "(919) 555-6789", "(214) 555-0123", "(407) 555-4567", "(612) 555-8901",
            "(503) 555-2345", "(303) 555-6789", "(619) 555-0123", "(215) 555-4567", "(312) 555-8901",
            "(713) 555-2345", "(415) 555-6789", "(213) 555-0123", "(702) 555-4567", "(704) 555-8901"
        ]
        EMAILS = [
            "emma.johnson@email.com", "liam.smith@email.com", "olivia.brown@email.com", "noah.williams@email.com",
            "ava.jones@email.com", "elijah.garcia@email.com", "sophia.miller@email.com", "james.davis@email.com",
            "isabella.rodriguez@email.com", "benjamin.martinez@email.com", "charlotte.hernandez@email.com",
            "lucas.lopez@email.com", "mia.gonzalez@email.com", "mason.wilson@email.com", "amelia.anderson@email.com",
            "ethan.thomas@email.com", "harper.taylor@email.com", "alexander.moore@email.com", "evelyn.jackson@email.com",
            "henry.martin@email.com", "abigail.lee@email.com", "sebastian.perez@email.com", "ella.thompson@email.com",
            "daniel.white@email.com", "scarlett.harris@email.com"
        ]
        generated = Customer(
            name=f'{random.choice(FIRST_NAMES)} {random.choice(LAST_NAMES)}',
            contact=random.choice(EMAILS),
            phone=random.choice(PHONES),
            address=random.choice(ADDRESSES)
        )
        generated.save()


class Item(GeneratingModel):
    ITEM_STATUS = [
        ('active', _('database.item.active')),
        ('inactive', _('database.item.inactive'))
    ]   
    
    # iid
    name = models.CharField(max_length=50, verbose_name=_('database.item.name'))
    category = models.CharField(max_length=50, verbose_name=_('database.item.category'))
    price = models.DecimalField(decimal_places=2,max_digits=6, verbose_name=_('database.item.price'))
    supplier = models.ForeignKey(Supplier,on_delete=models.SET_NULL,null=True, verbose_name=_('database.item.supplier'))
    status = models.CharField(max_length=10, choices=ITEM_STATUS, default='active', verbose_name=_('database.item.status'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('database.item.created_at'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('database.item.updated_at'))

    def __str__(self):
        return self.name
    
    def generate():
        NAMES = ["Widget", "Gadget", "Thingamajig", "Doohickey", "Whatchamacallit", "Contraption"]
        CATEGORIES = ["Electronics", "Clothing", "Books", "Home", "Toys", "Automotive", "Sports"]
        SUPPLIERS = list(Supplier.objects.all())
        
        generated = Item(
            name=f"{random.choice(NAMES)} {random.randint(1, 100)}",
            category=random.choice(CATEGORIES),
            price=random.uniform(5.00, 500.00),
            supplier=random.choice(SUPPLIERS) if SUPPLIERS else None,
            status=random.choice(['active', 'inactive'])
        )
        generated.save()

class Order(GeneratingModel):
    ORDER_STATUS = [
        ('pending', _('database.order.pending')),
        ('approved', _('database.order.approved')),
        ('delivered', _('database.order.delivered')),
        ('canceled', _('database.order.canceled'))
    ]
    
    # oid
    item = models.ForeignKey(Item,on_delete=models.SET_NULL,null=True, verbose_name=_('database.order.item'))
    customer = models.ForeignKey(Customer,on_delete=models.SET_NULL,null=True, verbose_name=_('database.order.customer'))
    order_date = models.DateTimeField(auto_now_add=True, verbose_name=_('database.order.order_date'))
    quantity = models.IntegerField(verbose_name=_('database.order.quantity'))
    status = models.CharField(max_length=10, choices=ORDER_STATUS, default='pending', verbose_name=_('database.order.status'))

    def __str__(self):
        return f'{self.item} ({self.status})'
    
    @property
    def full_price(self):
        if not self.item:
            return 0.0
        return float(self.item.price) * float(self.quantity)
    
    def generate():
        ITEMS = list(Item.objects.all())
        CUSTOMERS = list(Customer.objects.all())
        
        generated = Order(
            item=random.choice(ITEMS) if ITEMS else None,
            customer=random.choice(CUSTOMERS) if CUSTOMERS else None,
            quantity=random.randint(1, 50),
            status=random.choice(['pending', 'approved', 'delivered', 'canceled'])
        )
        generated.save()

class Warehouse(GeneratingModel):
    #wid
    name = models.CharField(max_length=50, verbose_name=_('database.warehouse.name'))
    location = models.CharField(max_length=50, verbose_name=_('database.warehouse.location'))

    def __str__(self):
        return self.name
    
    def generate():
        NAMES = ["Central Warehouse", "East Depot", "West Storage", "South Hub", "North Facility"]
        LOCATIONS = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"]
        
        generated = Warehouse(
            name=random.choice(NAMES),
            location=random.choice(LOCATIONS)
        )
        generated.save()

class Stocks(GeneratingModel):
    #sid
    item = models.ForeignKey(Item, on_delete=models.SET_NULL, null=True, verbose_name=_('database.stock.item'))
    warehouse = models.ForeignKey(Warehouse, on_delete=models.SET_NULL,null=True, verbose_name=_('database.stock.warehouse'))
    quantity = models.IntegerField(default=0, verbose_name=_('database.stock.quantity'))
    min_quantity = models.IntegerField(verbose_name=_('database.stock.min_quantity')) 

    def __str__(self):
        return f'{self.item.name}: {self.warehouse.name}'
    
    @property
    def name(self):
        return f'{self}'


    def generate():
        ITEMS = list(Item.objects.all())
        WAREHOUSES = list(Warehouse.objects.all())
        
        generated = Stocks(
            item=random.choice(ITEMS) if ITEMS else None,
            warehouse=random.choice(WAREHOUSES) if WAREHOUSES else None,
            quantity=random.randint(1, 500),
            min_quantity=random.randint(1, 50)
        )
        generated.save()
        
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__initial = self._dict

    @property
    def diff(self):
        d1 = self.__initial
        d2 = self._dict
        diffs = [(k, (v, d2[k])) for k, v in d1.items() if v != d2[k]]
        return dict(diffs)

    @property
    def has_changed(self):
        return bool(self.diff)

    @property
    def changed_fields(self):
        return self.diff.keys()

    def get_field_diff(self, field_name):
        """
        Returns a diff for field if it's changed and None otherwise.
        """
        return self.diff.get(field_name, None)

    def save(self, *args, **kwargs):
        """
        Saves model and set initial state.
        """
        if self.id is not None and 'update_fields' not in kwargs:
            kwargs.update({'update_fields': self.changed_fields})
            
        super().save(*args, **kwargs)
        self.__initial = self._dict

    @property
    def _dict(self):
        return model_to_dict(self, fields=[
            field.name
            for field in self._meta.get_fields()
        ])


class StocksHistory(models.Model):
    stock = models.ForeignKey(Stocks, on_delete=models.CASCADE, null=False, blank=False, verbose_name=_("database.stock_history.stock"))
    quantity_change = models.IntegerField(default=0, verbose_name=_("database.stock_history.quantity_change"))
    change_date = models.DateTimeField(auto_now_add=True, editable=False, verbose_name=_('database.stock_history.order_date'))

    def __str__(self):
        return f'{self.stock} ({self.change_date})'



class UserConfig(models.Model):
    CURRENCY = sorted([(c.lower(), iso4217parse.parse(c)[0].name) for c in CurrencyConverter().currencies if iso4217parse.parse(c) is not None], key=lambda i: i[1])

    language = models.CharField(max_length=10, choices=settings.LANGUAGES, default=settings.LANGUAGE_CODE, verbose_name=_('database.userconfig.language'))
    currency = models.CharField(max_length=5, choices=CURRENCY, default="eur", verbose_name=_('database.userconfig.currency'))
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'Config for {self.user}'