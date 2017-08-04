from product.models import Parent, Collection
from django import template
register = template.Library()


@register.inclusion_tag('includes/header.html')
def menu(request):
    nodes = Parent.objects.all()
    return {
        "nodes": nodes,
    }


@register.inclusion_tag('includes/header.html')
def collection(request):
    collect = Collection.objects.all()
    return {
        "collect": collect,
    }