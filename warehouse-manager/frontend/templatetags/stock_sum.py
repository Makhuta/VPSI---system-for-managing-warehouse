from django import template

register = template.Library()

@register.filter
def stock_sum(stock_history):
    return sum(float(s.stock.item.price) * s.quantity_change * -1 for s in stock_history)