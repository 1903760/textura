from django import forms
from .models import *
from .widgets import *


# форма загрузки фото в админку
class PhotoAdminForm(forms.ModelForm):

    class Meta:
        model = Photo
        widgets = {'image': MultiFileInput}
        exclude = [""]


# Форма фильтрации
class ProductSeachForm(forms.Form):
    category = forms.SlugField(label='Категория', required=False)
    name_product = forms.CharField(label='Название', required=False)
    min_price = forms.IntegerField(label="от", required=False)
    max_price = forms.IntegerField(label="до", required=False)
    ordering = forms.ChoiceField(label="сортировка", required=False, choices=[
        ["product__name", "по алфавиту"],
        ["product__price", "дешевые сверху"],
        ["-product__price", "дорогие сверху"]
    ])


class ProductAdd(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('name', 'category', 'price', 'description', 'composition')

