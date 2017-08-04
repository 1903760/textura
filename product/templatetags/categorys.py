from product.models import Parent
from django import template
register = template.Library()


@register.inclusion_tag('product/all_tpl.html')
def categorys():
    nodes = Parent.objects.all()
    return {
        "nodes": nodes,
    }
