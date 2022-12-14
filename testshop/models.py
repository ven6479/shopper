from django.db import models
from django.utils.translation import gettext_lazy as _
from .fields import WEBPField
from django.utils.text import slugify
import uuid
def image_folder(instance, filename):
    return 'images/product/{}.webp'.format(uuid.uuid4().hex)
class Product(models.Model):
    class Meta:
        verbose_name = _('product')
        verbose_name_plural = _('products')

        ordering = ['title']
    class Status(models.TextChoices):
        IN_STOCK = 'in_stock', _('in stock')
        ON_ORDER = 'on_order', _('on order')
        WAITING = 'waiting', _('waiting')
        NOT_IN_STOCK = 'not_in_stock', _('not in stock')
        NOT_MAKING = 'not_making', _('not making')

    title = models.CharField(_('title'), max_length=255)
    sku = models.CharField(_('sku'), max_length=255, unique=True)
    slug = models.SlugField(_('slug'), max_length=255,blank=True)
    category = models.ForeignKey(verbose_name=_('category'), to='Category', on_delete=models.PROTECT, related_name='products')
    status = models.CharField(_('status'),choices=Status.choices,max_length=255)
    price = models.DecimalField(_('price'),blank=True,decimal_places=2,max_digits=10,default='0.00')
    image = WEBPField(upload_to=image_folder,default=None)
    def save(self,*args,**kwargs):
        self.slug = slugify(self.title)+'-'+slugify(self.sku)
        super(Product, self).save(*args,**kwargs)
    def __str__(self):
        return self.title


class Category(models.Model):
    class Meta:
        verbose_name = _('category')
        verbose_name_plural = _('categories')

        ordering = ['title']

    title = models.CharField(_('title'), max_length=255)
    slug = models.SlugField(_('slug'), max_length=255)

    property_objects = models.ManyToManyField(verbose_name=_('properties'), to='PropertyObject')

    def __str__(self):
        return self.title


class PropertyObject(models.Model):
    class Meta:
        verbose_name = _('property object')
        verbose_name_plural = _('properties objects')

        ordering = ['title']

    class Type(models.TextChoices):
        STRING = 'string', _('string')
        DECIMAL = 'decimal', _('decimal')

    title = models.CharField(_('title'), max_length=255)
    code = models.SlugField(_('code'), max_length=255)
    value_type = models.CharField(_('value type'), max_length=10, choices=Type.choices)

    def __str__(self):
        return f'{self.title} ({self.get_value_type_display()})'


class PropertyValue(models.Model):
    class Meta:
        verbose_name = _('property value')
        verbose_name_plural = _('properties values')

        ordering = ['value_string', 'value_decimal']

    property_object = models.ForeignKey(to=PropertyObject, on_delete=models.PROTECT)

    value_string = models.CharField(_('value string'), max_length=255, blank=True, null=True)
    value_decimal = models.DecimalField(_('value decimal'), max_digits=11, decimal_places=2, blank=True, null=True)
    code = models.SlugField(_('code'), max_length=255)

    products = models.ManyToManyField(to=Product, related_name='properties')

    def __str__(self):
        return str(getattr(self, f'value_{self.property_object.value_type}', None))
# Create your models here.
