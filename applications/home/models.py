from django.db import models
# apps terceros
from model_utils.models import TimeStampedModel

# Create your models here.

class Home(TimeStampedModel):
    """Modelo para datos de la pantalla home"""

    title = models.CharField(
        'Nombre',
        max_length=30
    )
    description = models.TextField('Descripción')
    about_title = models.CharField(
        'Título Nosotros',
        max_length=50
    )
    about_text = models.TextField(
        'Contenido Nosotros',
        blank=True,
        null=True
    )
    phone = models.CharField(
        'Número de Contacto',
        max_length=20
    )

    class Meta:
        verbose_name = 'Página Principal'
        verbose_name_plural = 'Página Principal'
    
    def __str__(self):
        return self.title
    

class Suscribers(TimeStampedModel):
    """Suscripciones"""
    
    email = models.EmailField('Correo', max_length=100)

    class Meta:            
        verbose_name = 'Suscritor'
        verbose_name_plural = 'Suscriptores'
        
    def __str__(self):
        return self.email


class Contact(TimeStampedModel):
    """Formulario de Contacto"""

    full_name = models.CharField(
        'Nombres',
        max_length=60
    )
    email = models.EmailField(
        'Correo',
        max_length=100
    )
    message = models.TextField('Mensaje')

    class Meta:
        verbose_name = 'Contacto'
        verbose_name_plural = 'Mensajes'
    
    def __str__(self):
        return self.full_name
    

