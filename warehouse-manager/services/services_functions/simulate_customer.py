from database.models import Stocks
import random

def run(**kwargs):
    print("Simulatinc customers...")
    rng = random.randrange(1, 5)
    
    for round in range(rng):
        stocks = Stocks.objects.all()
        stocks_rng = random.randrange(1, len(stocks))
        
        stock_quantity = stocks[stocks_rng-1].quantity
        if stock_quantity <= 0:
            return
        stocks[stocks_rng-1].quantity -= random.randrange(1, stock_quantity)
        stocks[stocks_rng-1].save()