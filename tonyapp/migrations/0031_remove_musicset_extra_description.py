# Generated by Django 5.0.7 on 2024-12-05 23:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tonyapp', '0030_musicset_preview_link'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='musicset',
            name='extra_description',
        ),
    ]
