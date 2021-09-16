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


class Category(models.Model):
    category = models.CharField(_('category'), max_length=100)

    def __str__(self):
        return self.category

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Product(models.Model):
    name = models.CharField(_('name'), max_length=100, blank=False)
    price = models.DecimalField(_('price'), max_digits=8, decimal_places=2, blank=False)
    stock = models.IntegerField(_('stock'), blank=False)
    category = models.ForeignKey(Category, verbose_name=_('category'), blank=True, null=True, on_delete=models.SET_NULL)
    image = StdImageField(_('image'), upload_to=get_file_path, blank=True, variations={'thumb': (480, 480)})
    slug = models.SlugField('slug', max_length=100, editable=False)
    is_active = models.BooleanField(_('is active'), default=True)

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
