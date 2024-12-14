# Generated by Django 5.0.7 on 2024-12-02 17:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tonyapp', '0017_delete_cartitemunit'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='color',
        ),
        migrations.RemoveField(
            model_name='cartitem',
            name='size',
        ),
        migrations.CreateModel(
            name='CartItemVariation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(choices=[('S', 'Small'), ('M', 'Medium'), ('L', 'Large'), ('XL', 'Extra Large')], max_length=2)),
                ('color', models.CharField(choices=[('Red', 'Red'), ('Blue', 'Blue'), ('Black', 'Black'), ('White', 'White')], max_length=20)),
                ('cart_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='variations', to='tonyapp.cartitem')),
            ],
        ),
    ]
