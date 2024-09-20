from django.db import models, IntegrityError
from django.template.defaultfilters import slugify
from django.core.exceptions import ValidationError

class Category(models.Model):
    name = models.CharField(max_length=40)
    
    def __str__(self):
        try:
            return self.name
        except:
            pass

class Brand(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        try:
            return self.name
        except:
            pass

class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='nombre')
    price = models.IntegerField(verbose_name="precio")
    category = models.ForeignKey(to=Category, null=True, blank=False, on_delete=models.SET_NULL, verbose_name='categoría')
    brand = models.ForeignKey(to=Brand, null=True, blank=False, on_delete=models.SET_NULL, verbose_name='marca')
    slug = models.SlugField(editable=False)
    image_1 = models.FileField(blank=False, upload_to='products/images', verbose_name='imagen 1')
    image_2 = models.FileField(blank=True, upload_to='products/images', verbose_name='imagen 2')
    image_3 = models.FileField(blank=True, upload_to='products/images', verbose_name='imagen 3')
    characteristic_1 = models.CharField(max_length=100, blank=True, verbose_name='característica 1')
    characteristic_2 = models.CharField(max_length=100, blank=True, verbose_name='característica 2')
    characteristic_3 = models.CharField(max_length=100, blank=True, verbose_name='característica 3')
    isFeatured = models.BooleanField(default=False, verbose_name='producto destacado?')

    class Meta:
        verbose_name_plural = 'Productos'

    def __str__(self):
        try:
            return self.name
        except:
            return 'product'
    
    def save(self):
        try: 
            self.slug = slugify(self.name) # Can be made with AutoSlug as well. It would be the best
            super().save()
        except IntegrityError:
            raise ValidationError('Error saving')
