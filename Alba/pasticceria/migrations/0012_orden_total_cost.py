# Generated by Django 5.0.6 on 2024-06-22 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pasticceria', '0011_alter_producto_precio'),
    ]

    operations = [
        migrations.AddField(
            model_name='orden',
            name='total_cost',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]
