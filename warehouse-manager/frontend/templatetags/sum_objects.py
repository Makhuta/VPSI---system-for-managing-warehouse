from django import template

register = template.Library()

def get_value(obj, path):
    attributes = path.split(".")
    for attr in attributes:
        obj = getattr(obj, attr, None)
        if obj is None:
            return 0
    return obj


@register.filter
def sum_objects(objects, path):
    return sum(get_value(obj, path) for obj in objects)