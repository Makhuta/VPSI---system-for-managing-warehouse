from django import template

register = template.Library()

@register.filter
def critical_stocks(objects):
    return [o for o in objects if getattr(o, "quantity", 0) <= getattr(o, "min_quantity", 0)]