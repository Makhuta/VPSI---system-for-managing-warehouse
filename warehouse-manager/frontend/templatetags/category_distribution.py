from django import template
from collections import Counter

register = template.Library()

@register.filter
def category_distribution(items, args):
    '''
        how args work:
        if on args are empty                         => no data is provided 
        if only category is provided                 => provides all categories
        if only counts is provided                   => provides all counts
        if number is provided together with category => provides top n most frequent counts/categories
    '''
    
    parts = args.split(",")
    output_type = parts[0] if parts else ""
    top_n = int(parts[1]) if len(parts) > 1 else None

    category_counter = Counter(item.category for item in items)
    most_common = category_counter.most_common(top_n) if top_n else category_counter.items()

    if output_type == "labels":
        return [label for label, _ in most_common]
    elif output_type == "counts":
        return [count for _, count in most_common]
    
    return []
