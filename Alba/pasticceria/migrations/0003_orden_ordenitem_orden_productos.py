# Generated by Django 5.0.6 on 2024-06-06 00:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pasticceria', '0002_producto_vendedor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orden',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(auto_now_add=True)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ordenes', to='pasticceria.cliente')),
                ('vendedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ordenes', to='pasticceria.vendedor')),
            ],
        ),
        migrations.CreateModel(
            name='OrdenItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveIntegerField()),
                ('orden', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pasticceria.orden')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pasticceria.producto')),
            ],
        ),
        migrations.AddField(
            model_name='orden',
            name='productos',
            field=models.ManyToManyField(through='pasticceria.OrdenItem', to='pasticceria.producto'),
        ),
    ]
