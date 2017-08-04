from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_delete

# Create your models here.
class Slider(models.Model):
    name = models.CharField(verbose_name="Название", default=None, blank=True, max_length=100)
    image = models.ImageField('изображение', upload_to='slider/photos')
    url = models.URLField(verbose_name='ссылка', null=True)

    class Meta:
        verbose_name = "Слайдер"
        verbose_name_plural="Слайдеры"

    def __str__(self):
        return self.name

@receiver(post_delete, sender=Slider)
def photo_post_delete_handler(sender, **kwargs):
    photo = kwargs['instance']
    storage, path = photo.image.storage, photo.image.path
    storage.delete(path)