# Generated by Django 5.0.6 on 2024-06-09 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pasticceria', '0008_alter_cliente_telefono'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='telefono',
            field=models.CharField(max_length=15, null=True, verbose_name='Telefono'),
        ),
    ]