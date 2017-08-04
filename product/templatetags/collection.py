from product.models import Parent
from django import template
register = template.Library()


@register.inclusion_tag('product/call_tpl.html')
def collections():
    nodes = Parent.objects.all()
    return {
        "nodes": nodes,
    }
