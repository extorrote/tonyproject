# Generated by Django 5.0.7 on 2024-11-29 20:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tonyapp', '0005_alter_cartitem_cart_alter_cartitem_price_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='cart',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='tonyapp.cart'),
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='product_id',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='quantity',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AlterUniqueTogether(
            name='cartitem',
            unique_together={('cart', 'product_type', 'product_id')},
        ),
    ]