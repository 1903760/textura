from product.models import Parent
from django import template
register = template.Library()


@register.inclusion_tag('product/discounts_tpl.html')
def discounts():
    nodes = Parent.objects.all()
    return {
        "nodes": nodes,
    }
