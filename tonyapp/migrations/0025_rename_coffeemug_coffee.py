# Generated by Django 5.0.7 on 2024-12-05 17:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tonyapp', '0024_rename_musicset_set'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CoffeeMug',
            new_name='Coffee',
        ),
    ]