from django.core.management.base import BaseCommand
from database.models import *
from database.functions import generate_model

class Command(BaseCommand):
    help = 'Creates specified number of items in DB.'

    def add_arguments(self, parser):
        parser.add_argument('amount', type=int, help='Amount of items to generate')

    def handle(self, *args, **kwargs):
        # Get the arguments
        amount = int(kwargs['amount'])

        generate_model(Supplier, amount)
        generate_model(Item, amount)
        generate_model(Customer, amount)
        generate_model(Order, amount)
        generate_model(Warehouse, amount)
        generate_model(Stocks, amount)