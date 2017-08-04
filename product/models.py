from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver
from colorful.fields import RGBColorField
# from mptt.models import MPTTModel, TreeForeignKey
# import mptt
from easy_thumbnails.fields import ThumbnailerImageField
# Create your models here.


class Collection(models.Model):
    name = models.CharField(verbose_name='Коллекция', max_length=150, default=None)
    slug = models.SlugField(verbose_name='ссылка')
    is_active = models.BooleanField(verbose_name='Статус активности', default=True)

    class Meta:
        db_table = 'collection'
        verbose_name = 'Коллекция'
        verbose_name_plural = 'Коллекции'
        ordering = ('name',)

    def __str__(self):
        return self.name


class Parent(models.Model):
    name = models.CharField(verbose_name='Категория', max_length=150, default=None)
    slug = models.SlugField(verbose_name='ссылка')
    is_active = models.BooleanField(verbose_name='Статус активности', default=True)

    class Meta:
        db_table = 'parent'
        verbose_name = 'Категория категории'
        verbose_name_plural = 'Категории категории'
        ordering = ('name',)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(verbose_name='Категория', max_length=150, default=None)
    parent = models.ForeignKey(Parent, verbose_name="Родитель")
    slug = models.SlugField(verbose_name='ссылка')
    is_active = models.BooleanField(verbose_name='Статус активности', default=True)

    class Meta:
        db_table = 'category'
        verbose_name = 'Категория товара'
        verbose_name_plural = 'Категории товаров'
        ordering = ('parent',)

    def __str__(self):
        return '%s/%s' % (self.parent.name, self.name)


class Product(models.Model):
    name = models.CharField('название товара', max_length=200)
    category = models.ForeignKey(Category, blank=True, null=True, verbose_name='Категория')
    collection = models.ForeignKey(Collection, blank=True, null=True, verbose_name='Коллекция')
    # category = TreeForeignKey(Category, blank=True, null=True, related_name='cat', verbose_name='Категория')
    price = models.IntegerField(verbose_name='цена в ₸', default=0)
    recommended = models.BooleanField(verbose_name='Рекомендуемый товар', default=False)
    description = models.TextField(verbose_name='описание', help_text='Напишите описание товара', blank=True,
                                   default=None)
    composition = models.TextField(verbose_name='Состав', max_length=400, blank=True, default=None)
    is_active = models.BooleanField(verbose_name='Статус активный', default=True)
    created = models.DateTimeField('Дата создания', auto_now_add=True)
    updated = models.DateTimeField('Дата обновления', auto_now=True)


    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['created']

    def __str__(self):
        return self.name


class Color(models.Model):
    product = models.ForeignKey(Product)
    color = RGBColorField(verbose_name='цвет')

    def __str__(self):
        return '%s' % self.id

    class Meta:
        verbose_name = 'Цвет'
        verbose_name_plural = 'Цвета'


class Photo(models.Model):
    product = models.ForeignKey(Product, related_query_name='Товар', verbose_name='Товар')
    image = ThumbnailerImageField('изображение', upload_to='product/photos')
    is_main = models.BooleanField('Главное фото', default=False, blank=True)
    is_active = models.BooleanField(verbose_name='Статус активный', default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def image_img(self):
        if self.image:
            return u'<a href="{0}" target="_blank"><img src="{0}" width="100"/></a>'.format(self.image.url)
        else:
            return '(Нет изображения)'

    image_img.short_description = 'Картинка'
    image_img.allow_tags = True

    def __str__(self):
        return '%s' % self.id

    class Meta:
        verbose_name = 'Фото'
        verbose_name_plural = 'Фотографии'
        # ordering = ['title_product']


@receiver(post_delete, sender=Photo)
def photo_post_delete_handler(sender, **kwargs):
    photo = kwargs['instance']
    storage, path = photo.image.storage, photo.image.path
    storage.delete(path)


class Offer(models.Model):
    product = models.ForeignKey(Product)
    SIZE_CHOICES = (
         ('25', '25'), ('26', '26'), ('27', '27'), ('28', '28'), ('29', '29'), ('30', '30'), ('31', '31'), ('32', '32'),
         ('33', '33'), ('34', '34'), ('35', '35'), ('36', '36'), ('37', '37'), ('38', '38'), ('39', '39'), ('40', '40'),
         ('41', '41'), ('42', '42'), ('43', '43'), ('44', '44'), ('45', '45'), ('46', '46'), ('47', '47'), ('48', '48'),
         ('49', '49'), ('50', '50'), ('51', '51'), ('52', '52'), ('53', '53'), ('54', '54'), ('55', '55'), ('56', '56'),
         ('57', '57'), ('58', '58'), ('59', '59'), ('60', '60'), ('61', '61'), ('62', '62'), ('63', '63'), ('64', '64'),
         ('65', '65'), ('66', '66'), ('67', '67'), ('68', '68'), ('69', '69'), ('70', '70'), ('71', '71'), ('72', '72'),
         ('73', '73'), ('74', '74'), ('75', '75'), ('76', '76'), ('77', '77'), ('78', '78'), ('79', '79'), ('80', '80'),
         ('81', '81'), ('82', '82'), ('83', '83'), ('84', '84'), ('85', '85'), ('86', '86'), ('87', '87'), ('88', '88'),
         ('89', '89'), ('90', '90'), ('91', '91'), ('92', '92'), ('93', '93'), ('94', '94'), ('95', '95'), ('96', '96'),
         ('97', '97'), ('98', '98'), ('99', '99')
    )
    CHOICES = (
        ('XS', 'XS'), ('S', 'S'), ('M', 'M'), ('L', 'L'), ('XL', 'XL'), ('XXL', 'XXL'), ('XXL', 'XXL'),
        ('XXXL', 'XXXL'),
    )
    size = models.CharField(verbose_name='размер', blank=True, default=None, max_length=3, choices=SIZE_CHOICES)
    type_choices = models.CharField(verbose_name='Тип размера',max_length=6, default=None, blank=True, choices=CHOICES)
    width = models.IntegerField(verbose_name='ширина', default=None, blank=True, null=True)
    height = models.IntegerField(verbose_name='высота', default=None, blank=True, null=True)

    class Meta:
        verbose_name = 'Размер товара'
        verbose_name_plural = 'Размеры товара'
        ordering = ['type_choices']

    def __str__(self):
        return '%s' % self.id
