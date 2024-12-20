# Generated by Django 5.0.7 on 2024-11-29 19:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tonyapp', '0004_cart_session_key'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='cart',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tonyapp.cart'),
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='product_id',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='product_type',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='quantity',
            field=models.PositiveIntegerField(),
        ),
    ]
