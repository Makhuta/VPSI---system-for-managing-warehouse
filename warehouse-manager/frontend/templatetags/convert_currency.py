from django import template
from currency_converter import CurrencyConverter

register = template.Library()


@register.filter
def convert_currency(value, arg):
    c = CurrencyConverter()
    from_c = 'EUR'
    to_c = arg.upper()
    try:
        return f'{c.convert(value, from_c, to_c):,.2f} {to_c}'.replace(",", " ")
    except:
        return f'{value:,.2f} {from_c}'.replace(",", " ")