# Generated by Django 5.0.7 on 2024-11-30 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tonyapp', '0008_remove_cart_session_key_remove_cart_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='color',
            field=models.CharField(blank=True, choices=[('red', 'Red'), ('blue', 'Blue'), ('green', 'Green'), ('black', 'Black')], max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='cartitem',
            name='size',
            field=models.CharField(blank=True, choices=[('S', 'Small'), ('M', 'Medium'), ('L', 'Large'), ('XL', 'X-Large')], max_length=10, null=True),
        ),
    ]