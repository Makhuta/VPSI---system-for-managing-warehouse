from django import template
from datetime import date, timedelta

register = template.Library()

@register.filter
def sales_chart_data(orders, data_type):
    """Returns earnings or costs over the last 7 days."""
    today = date.today()
    last_7_days = [today - timedelta(days=i) for i in reversed(range(7))]
    result = []

    for day in last_7_days:
        day_orders = [o for o in orders if o.order_date.date() == day]
        if data_type == "earnings":
            value = sum(float(o.item.price) * o.quantity for o in day_orders if o.status == "delivered")
        elif data_type == "costs":
            value = sum(float(o.item.price) * o.quantity for o in day_orders if o.status == "pending")
        else:
            value = 0
        result.append(value)

    return result