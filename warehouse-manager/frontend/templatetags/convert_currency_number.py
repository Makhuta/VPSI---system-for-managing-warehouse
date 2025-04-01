from django import template
from currency_converter import CurrencyConverter

register = template.Library()


@register.filter
def convert_currency_number(values, arg):
    print("here")
    c = CurrencyConverter()
    from_c = 'EUR'
    to_c = arg.upper()
    from currency_symbols import CurrencySymbols
    try:
        return [c.convert(value, from_c, to_c) for value in values]
    except:
        return values