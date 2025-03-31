

def run(**kwargs):
    print("Sending stock history")
    """
    from warehouse.models import StockHistory
    from django.core.mail import send_mail
    
    history_entries = StockHistory.objects.filter(timestamp__gt=now() - timedelta(days=1))
    
    if history_entries.exists():
        email_body = "\n".join([str(entry) for entry in history_entries])
        send_mail("Stock Update", email_body, "noreply@example.com", ["admin@example.com"])
    """