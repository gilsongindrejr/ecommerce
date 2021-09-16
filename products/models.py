import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _
from stdimage import StdImageField
from django.template.defaultfilters import slugify
from django.db.models import signals


def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = uuid.uuid4()
    return f'products/{filename}.{ext}'


class Product(models.Model):
    name = models.CharField(_('name'), max_length=100)
    price = models.DecimalField(_('price'), max_digits=8, decimal_places=2)
    stock = models.IntegerField(_('stock'))
    image = StdImageField(_('image'), upload_to=get_file_path, variations={'thumb': (480, 480)})
    slug = models.SlugField('slug', max_length=100, editable=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')


def product_pre_save(signal, instance, sender, **kwargs):
    if not instance.id:
        instance.slug = slugify(instance.name)


# Signals
signals.pre_save.connect(product_pre_save, sender=Product)
