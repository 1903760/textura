import django_filters
from .models import Product

CHOICES =[
        ["name", "по алфавиту"],
        ["price", "дешевые сверху"],
        ["-price", "дорогие сверху"]
]


class ProductFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(name='name', lookup_expr='icontains')
    category__slug = django_filters.CharFilter()
    price__gt = django_filters.NumberFilter(name='price', lookup_expr='gt')
    price__lt = django_filters.NumberFilter(name='price', lookup_expr='lt')
    ordering = django_filters.OrderingFilter(choices=CHOICES, required=True, empty_label=None,)

    class Meta:
        model = Product
        exclude = [field.name for field in Product._meta.fields]
        order_by_field = 'name'

