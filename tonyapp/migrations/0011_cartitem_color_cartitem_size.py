# Generated by Django 5.0.7 on 2024-11-30 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tonyapp', '0010_remove_cartitem_color_remove_cartitem_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='color',
            field=models.CharField(blank=True, choices=[('Red', 'Red'), ('Blue', 'Blue'), ('Black', 'Black'), ('White', 'White')], max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='cartitem',
            name='size',
            field=models.CharField(blank=True, choices=[('S', 'Small'), ('M', 'Medium'), ('L', 'Large'), ('XL', 'Extra Large')], max_length=2, null=True),
        ),
    ]