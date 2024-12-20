# Generated by Django 5.0.7 on 2024-12-04 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tonyapp', '0020_rename_cover_image_album_image_alter_album_songs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clothing',
            name='color',
            field=models.CharField(blank=True, choices=[('Red', 'Red'), ('Blue', 'Blue'), ('Black', 'Black'), ('White', 'White')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='clothing',
            name='size',
            field=models.CharField(blank=True, choices=[('S', 'Small'), ('M', 'Medium'), ('L', 'Large'), ('XL', 'Extra Large')], max_length=2, null=True),
        ),
    ]
