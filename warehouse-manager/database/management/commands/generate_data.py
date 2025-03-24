from django.core.management.base import BaseCommand
from database.models import *

class Command(BaseCommand):
    help = 'Creates a custom superuser if one doesn\'t already exist.'

    def add_arguments(self, parser):
        parser.add_argument('amount', type=int, help='Amount of items to generate')

    def handle(self, *args, **kwargs):
        # Get the arguments
        amount = int(kwargs['amount'])

        
        for i in range(amount):
            Supplier.generate()
            
            
        for i in range(amount):
            Item.generate()
            
            
        for i in range(amount):
            Order.generate()
            
            
        for i in range(amount):
            Warehouse.generate()
            
            
        for i in range(amount):
            Stocks.generate()