# Generated by Django 4.1 on 2022-08-16 03:09

from django.db import migrations, models
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('full_name', models.CharField(max_length=60, verbose_name='Nombres')),
                ('email', models.EmailField(max_length=100, verbose_name='Correo')),
                ('message', models.TextField(verbose_name='Mensaje')),
            ],
            options={
                'verbose_name': 'Contacto',
                'verbose_name_plural': 'Mensajes',
            },
        ),
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('title', models.CharField(max_length=30, verbose_name='Nombre')),
                ('description', models.TextField(verbose_name='Descripción')),
                ('about_title', models.CharField(max_length=50, verbose_name='Título Nosotros')),
                ('about_text', models.TextField(blank=True, null=True, verbose_name='Contenido Nosotros')),
                ('phone', models.CharField(max_length=20, verbose_name='Número de Contacto')),
            ],
            options={
                'verbose_name': 'Página Principal',
                'verbose_name_plural': 'Página Principal',
            },
        ),
        migrations.CreateModel(
            name='Suscribers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('email', models.EmailField(max_length=100, verbose_name='Correo')),
            ],
            options={
                'verbose_name': 'Suscritor',
                'verbose_name_plural': 'Suscriptores',
            },
        ),
    ]
