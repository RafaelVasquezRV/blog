# standard library
from datetime import timedelta, datetime
#
from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
#
from django.template.defaultfilters import slugify
# apps terceros
from model_utils.models import TimeStampedModel
from ckeditor_uploader.fields import RichTextUploadingField
from PIL import Image
# managers
from .managers import EntryManager

# Create your models here.

class Category(TimeStampedModel):
    """Categorías de una entrada"""

    short_name = models.CharField(
        'Nombre corto',
        max_length=15
    )
    name = models.CharField(
        'Nombre',
        max_length=50
    )

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'
    
    def __str__(self):
        return self.name


class Tag(TimeStampedModel):
    """Etiquetas de un artículo"""

    name = models.CharField(
        'Nombre',
        max_length=30
    )

    class Meta:
        verbose_name = 'Etiqueta'
        verbose_name_plural = 'Tags'

    def __str__(self):
        return self.name


class Entry(TimeStampedModel):
    """Modelo para entradas o artículos"""

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
    )
    tag = models.ManyToManyField(Tag)
    title = models.CharField(
        'Título',
        max_length=200
    )
    resume = models.TextField('Resumen')
    content = RichTextUploadingField('Contenido')
    public = models.BooleanField(default=False)
    image = models.ImageField(
        'Imagen',
        upload_to='Entry'
    )
    portada = models.BooleanField(default=False)
    in_home = models.BooleanField(default=False)
    slug = models.SlugField(editable=False, max_length=300)

    objects = EntryManager()

    class Meta:
        verbose_name = 'Entrada'
        verbose_name_plural = 'Entradas'
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        # calculamos el toral de segundos de la hora actual
        now = datetime.now()
        total_time = timedelta(
            hours=now.hour,
            minutes=now.minute,
            seconds=now.second,
        )
        seconds = int(total_time.total_seconds())
        slug_unique = '%s %s' % (self.title, str(seconds))
        
        self.slug = slugify(slug_unique)

        return super(Entry, self).save(*args, **kwargs)
    

def optimize_image(sender, instance, **kwargs):
    print('=====Función optimize_image========')
    print(instance)
    if instance.image:
        image = Image.open(instance.image.path)
        image.save(instance.image.path, quality=20, optimize=True)

post_save.connect(optimize_image, sender=Entry) # Clase 152