import django_filters
from .models import Photo

CHOICES =[
        ["product__name", "по алфавиту"],
        ["product__price", "дешевые сверху"],
        ["-product__price", "дорогие сверху"]
]


class ProductFilter(django_filters.FilterSet):
    product__name__icontains = django_filters.CharFilter(lookup_expr='icontains')
    product__category__slug = django_filters.CharFilter()
    product__price__gt = django_filters.NumberFilter(name='product__price', lookup_expr='gt')
    product__price__lt = django_filters.NumberFilter(name='product__price', lookup_expr='lt')
    ordering = django_filters.OrderingFilter(choices=CHOICES, required=True, empty_label=None,)

    class Meta:
        model = Photo
        exclude = [field.name for field in Photo._meta.fields]
        order_by_field = 'product__name'

