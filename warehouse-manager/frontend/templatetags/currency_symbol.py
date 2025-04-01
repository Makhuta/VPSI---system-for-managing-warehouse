from django import template

register = template.Library()


@register.filter
def currency_symbol(arg):
    from currency_symbols import CurrencySymbols
    try:
        return CurrencySymbols.get_symbol(arg.upper())
    except:
        return CurrencySymbols.get_symbol('EUR')