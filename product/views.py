from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404, render
from .models import *
from .filters import *
from django_filters.views import FilterView
from banner.models import Banner
from slider.models import Slider


class IndexViews(ListView):
    template_name = 'product/main.html'
    model = Product

    def get_context_data(self, **kwargs):
        context = super(IndexViews, self).get_context_data(**kwargs)
        context['sliders'] = Slider.objects.all()
        context['banners'] = Banner.objects.all()[:3]
        context['pass'] = Parent.objects.all()
        context['products'] = Photo.objects.filter(is_main=True, is_active=True, product__recommended=True)
        return context


class ProductDetailView(DetailView):
    model = Product

    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        context['photos'] = self.object.photo_set.all()
        context['colors'] = self.object.color_set.all()
        context['offers'] = self.object.offer_set.all()
        return context


class CategoryProductViews(FilterView):
    template_name = 'product/product_list.html'
    model = Product
    paginate_by = 10
    filterset_class = ProductFilter
    context_object_name = 'products'

    def get_queryset(self):
        qs = self.model.objects.prefetch_related('photo_set')
        if self.kwargs.get('motel_slug'):
            qs = qs.filter(category__parent__slug=self.kwargs['motel_slug'])
        if self.kwargs.get('cat_slug'):
            qs = qs.filter(category__slug=self.kwargs['cat_slug'])
        return qs


class CollectionViews(FilterView):
    template_name = 'product/coolections.html'
    model = Product
    paginate_by = 10
    filterset_class = ProductFilter
    context_object_name = 'products'

    def get_queryset(self):
        qs = self.model.objects.prefetch_related('photo_set')
        if self.kwargs.get('collec_slug'):
            qs = qs.filter(collection__slug=self.kwargs['collec_slug'])
        if self.kwargs.get('cat_slug'):
            qs = qs.filter(category__slug=self.kwargs['cat_slug'])
        return qs


class DiscountProductViews(FilterView):
    template_name = 'product/discounts_list.html'
    model = Product
    paginate_by = 10
    filterset_class = ProductFilter
    context_object_name = 'products'

    def get_queryset(self):
        qs = self.model.objects.prefetch_related('photo_set')
        if self.kwargs.get('motel_slug'):
            qs = qs.filter(category__parent__slug=self.kwargs['motel_slug'])
        if self.kwargs.get('cat_slug'):
            qs = qs.filter(category__slug=self.kwargs['cat_slug'])
        return qs


def product_list(request):
    filter = ProductFilter(request.GET, queryset=Product.objects.all())
    return render(request, 'product/rrr.html', {'filter': filter})