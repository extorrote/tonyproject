# Generated by Django 5.0.7 on 2024-12-01 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tonyapp', '0014_cart_is_active'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cartitem',
            options={'verbose_name': 'Cart Item', 'verbose_name_plural': 'Cart Items'},
        ),
        migrations.RemoveField(
            model_name='cart',
            name='is_active',
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
    ]
