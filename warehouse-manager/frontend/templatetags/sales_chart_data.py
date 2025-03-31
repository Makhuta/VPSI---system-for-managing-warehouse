from django import template
from datetime import date, timedelta

register = template.Library()

@register.filter
def sales_chart_data(stock_history, data_type):
    """Returns earnings or costs over the last 7 days."""
    today = date.today()
    last_7_days = [today - timedelta(days=i) for i in reversed(range(7))]
    result = []

    for day in last_7_days:
        day_stock = [s for s in stock_history if s.change_date.date() == day]

        if data_type == "earnings":
            value = sum(float(s.stock.item.price) * abs(s.quantity_change) for s in day_stock if s.quantity_change <= 0)
        elif data_type == "costs":
            value = sum(float(s.stock.item.price) * s.quantity_change for s in day_stock if s.quantity_change >= 0)
        else:
            value = 0
        result.append(value)

    return result