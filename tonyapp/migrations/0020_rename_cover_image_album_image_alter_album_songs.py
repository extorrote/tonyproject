# Generated by Django 5.0.7 on 2024-12-03 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tonyapp', '0019_cartitem_color_cartitem_size_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='album',
            old_name='cover_image',
            new_name='image',
        ),
        migrations.AlterField(
            model_name='album',
            name='songs',
            field=models.TextField(blank=True, null=True),
        ),
    ]
