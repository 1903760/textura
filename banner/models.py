from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_delete

# Create your models here.


class Banner(models.Model):
    name = models.CharField(verbose_name="Название", default=None, blank=True, max_length=100)
    image = models.ImageField('изображение', upload_to='banner/photos')
    url = models.URLField(verbose_name='ссылка', null=True, default=None)

    class Meta:
        verbose_name = "Баннер"
        verbose_name_plural = "Баннеры"

    def __str__(self):
        return self.name

@receiver(post_delete, sender=Banner)
def photo_post_delete_handler(sender, **kwargs):
    photo = kwargs['instance']
    storage, path = photo.image.storage, photo.image.path
    storage.delete(path)