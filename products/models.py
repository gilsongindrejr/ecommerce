import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _
from stdimage import StdImageField
from django.template.defaultfilters import slugify


# Could have used users.models.get_file_path function
# Decided to create another to keep file independence
def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = uuid.uuid4()
    return f'products/{filename}.{ext}'


class Product(models.Model):
    name = models.CharField(_('name'), max_length=100, blank=False)
    price = models.DecimalField(_('price'), max_digits=8, decimal_places=2, blank=False)
    stock = models.IntegerField(_('stock'), blank=False)
    image = StdImageField(_('image'), upload_to=get_file_path, variations={'thumb': (480, 480)})
    slug = models.SlugField('slug', max_length=100, editable=False)

    def __str__(self):
        return self.name

    # Check if product already exists before override save method to add slug
    # Could have done with signals, but its simpler and easier to test and does the same
    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)

    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')
