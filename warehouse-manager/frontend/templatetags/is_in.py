from django import template

register = template.Library()

@register.filter
def is_in(objects, value):
    key, in_list_str = value.split(",", 1)
    in_list = in_list_str.split(",")
    return [o for o in objects if getattr(o, key, None) in in_list]