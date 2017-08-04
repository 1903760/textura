from product.models import Parent
from django import template
register = template.Library()


@register.inclusion_tag('includes/header.html')
def menu(request):
    nodes = Parent.objects.all()
    return {
        "nodes": nodes,
    }

