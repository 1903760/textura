from django.contrib import admin
from .forms import *
from django.shortcuts import redirect
# from mptt.admin import DraggableMPTTAdmin
# from mptt.admin import TreeRelatedFieldListFilter


@admin.register(Parent)
class ParentAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Category)
class CatatgoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    suit_classes = 'suit-tab suit-tab-categorys'
    search_fields = ('name', 'parent')

# admin.site.register(Category, CatatgoryAdmin,
#                     prepopulated_fields={'slug': ('name',)},
#                     mptt_level_indent=20,
#                     list_display=(
#                         'tree_actions',
#                         'indented_title'),
#                     list_display_links=(
#                         'indented_title',
#                     ),
#                     )


# Цвет
class ColorInline(admin.StackedInline):
    suit_classes = 'suit-tab suit-tab-colors'
    show_change_link = True
    model = Color
    extra = 0


# Предложение
class OfferInline(admin.StackedInline):
    suit_classes = 'suit-tab suit-tab-offers'
    model = Offer
    extra = 0


# Фото
class PhotoInline(admin.TabularInline):
    suit_classes = 'suit-tab suit-tab-photos'
    show_change_link = True
    readonly_fields = ['image_img', ]
    list_display = ['image_img']
    model = Photo
    extra = 0


# админка товара
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    search_fields = ('name', 'category')
    exclude = ['id']
    suit_classes = 'suit-tab suit-tab-products'
    list_display = ['name', 'category', 'price', 'discount', 'discount_price', 'collection']
    # list_filter = (('category', TreeRelatedFieldListFilter),)
    list_filter = ('category',)
    inlines = [ColorInline, PhotoInline, OfferInline]
    extra = 1
    show_full_result_count = True

    class Meta:
        js = ('http://code.jquery.com/jquery-1.3.2.min.js',
              'js/jquery.js', 'media/inlines.js',)

    fieldsets = [
        (None, {
            'classes': ('suit-tab', 'suit-tab-general',),
            'fields': [
                'name',
                'category',
                'collection',
                'price',
                # 'discount_price',
                'discount',
                'recommended',
                'description',
                'composition',
                'is_active',
            ]
        }),
    ]
    suit_form_tabs = (('general', 'Товары'), ('photos', 'Фотки'), ('colors', 'Цвета'), ('offers', 'Размеры'))


    # Or bit more advanced example
    def suit_row_attributes(self, obj, request):
        css_class = {
            1: 'success',
            0: 'warning',
            -1: 'error',
        }.get(obj.is_active)
        if css_class:
            return {'class': css_class, 'name': obj.name}

    def suit_cell_attributes(self, obj, column):
        if column == 'countries':
            return {'class': 'text-center'}
        elif column == 'name' and obj.is_active == -1:
            return {'class': 'text-error'}

    def in_discount_price(self):
        return Product





# админка фото
@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    form = PhotoAdminForm
    search_fields = ('product__name', 'product__category__name',)
    list_display = ['id', 'product', 'image_img', 'is_main', 'is_active']
    show_full_result_count = True
    list_filter = ('image', ('product', admin.RelatedOnlyFieldListFilter),)

    def add_view(self, request, *args, **kwargs):
        images = request.FILES.getlist('image',[])
        is_valid = PhotoAdminForm(request.POST, request.FILES).is_valid()

        if request.method == 'GET' or len(images) <= 1 or not is_valid:
            return super(PhotoAdmin, self).add_view(request, *args, **kwargs)
        for image in images:
            product_id = request.POST['product']
            photo = Photo(product_id=product_id, image=image)
            photo.save()
        return redirect('/admin/product/photo/')
