# Generated by Django 5.0.7 on 2024-11-29 22:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tonyapp', '0007_alter_cartitem_unique_together_alter_cartitem_cart_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='session_key',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='user',
        ),
        migrations.RemoveField(
            model_name='cartitem',
            name='price',
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='cart',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cart_items', to='tonyapp.cart'),
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='product_id',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='product_type',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='quantity',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
