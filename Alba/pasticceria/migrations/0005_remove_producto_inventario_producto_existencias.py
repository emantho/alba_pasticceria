# Generated by Django 5.0.6 on 2024-06-06 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pasticceria', '0004_remove_producto_rating_alter_producto_descripcion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='inventario',
        ),
        migrations.AddField(
            model_name='producto',
            name='existencias',
            field=models.IntegerField(null=True, verbose_name='Existencias'),
        ),
    ]
