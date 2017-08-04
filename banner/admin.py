from django.contrib import admin
from .models import Banner
# Register your models here.

@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ['name', 'id']
    extra = 1
    show_full_result_count = True