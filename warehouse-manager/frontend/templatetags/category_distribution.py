from django import template
from datetime import date, timedelta

register = template.Library()

@register.filter
def category_distribution(items, output_type):
    """Returns either category labels or counts."""
    category_counter = {}
    for item in items:
        cat = item.category
        if cat in category_counter:
            category_counter[cat] += 1
        else:
            category_counter[cat] = 1

    if output_type == "labels":
        return list(category_counter.keys())
    elif output_type == "counts":
        return list(category_counter.values())
    return []