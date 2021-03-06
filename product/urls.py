from django.conf.urls import url
from .views import *


urlpatterns = [
    url(r'^$', IndexViews.as_view(), name='products_views'),
    url(r'^all/$', CategoryProductViews.as_view(), name='all_products'),
    url(r'^all/(?P<motel_slug>[-\w]+)/$', CategoryProductViews.as_view(), name='category_get'),
    url(r'^all/(?P<motel_slug>[-\w]+)/(?P<cat_slug>[-\w]+)/$', CategoryProductViews.as_view(), name='category'),
    url(r'^collection/$', CollectionViews.as_view(), name='all_collection'),
    url(r'^collection/(?P<collec_slug>[-\w]+)/$', CollectionViews.as_view(), name='collection_get'),
    url(r'^collection/(?P<collec_slug>[-\w]+)/(?P<cat_slug>[-\w]+)/$', CollectionViews.as_view(), name='collec_cat'),
    url(r'^discount/$', DiscountProductViews.as_view(), name='all_discounts'),
    url(r'^discount/(?P<motel_slug>[-\w]+)/$', DiscountProductViews.as_view(), name='d_category_get'),
    url(r'^discount/(?P<motel_slug>[-\w]+)/(?P<cat_slug>[-\w]+)/$', DiscountProductViews.as_view(), name='d_category'),
    url(r'product/(?P<pk>\d+)/$', ProductDetailView.as_view(), name='product'),
    url(r'qqqqqq/$', product_list),
]
