# Generated by Django 5.0.7 on 2024-11-29 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tonyapp', '0003_alter_cart_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='session_key',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
    ]
