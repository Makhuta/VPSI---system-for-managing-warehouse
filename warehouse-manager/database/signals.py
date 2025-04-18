from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from database.models import Stocks, StocksHistory
    
@receiver(post_save, sender=Stocks)
def add_jobs(sender, instance, update_fields=None, **kwargs):
    if update_fields and not all([field in ["quantity"] for field in list(update_fields)]):
        print(f"Changes ignored for {instance}, no relevant field changed.")
        return
    print(f'Updated Stocks: {instance.name}')
    
    stock_history = StocksHistory(stock=instance, quantity_change=(instance.diff.get("quantity", [0, 0])[1] - instance.diff.get("quantity", [0, 0])[0]))
    if stock_history.quantity_change != 0:
        stock_history.save()