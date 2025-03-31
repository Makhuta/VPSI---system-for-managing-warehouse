from django import template
from currency_converter import CurrencyConverter

register = template.Library()


@register.filter
def convert_currency(value, arg):
    c = CurrencyConverter()
    from_c = 'EUR'
    to_c = arg.upper()
    from currency_symbols import CurrencySymbols
    try:
        return f'{c.convert(value, from_c, to_c):,.2f} {CurrencySymbols.get_symbol(to_c)}'.replace(",", " ")
    except:
        return f'{value:,.2f} {CurrencySymbols.get_symbol(to_c)}'.replace(",", " ")