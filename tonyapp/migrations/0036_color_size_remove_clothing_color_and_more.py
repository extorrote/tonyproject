# Generated by Django 5.0.7 on 2024-12-10 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tonyapp', '0035_remove_cartitem_user_info_alter_cartitem_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(choices=[('Red', 'Red'), ('Blue', 'Blue'), ('Black', 'Black'), ('White', 'White')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(choices=[('S', 'Small'), ('M', 'Medium'), ('L', 'Large'), ('XL', 'Extra Large')], max_length=2)),
            ],
        ),
        migrations.RemoveField(
            model_name='clothing',
            name='color',
        ),
        migrations.RemoveField(
            model_name='clothing',
            name='size',
        ),
        migrations.AddField(
            model_name='clothing',
            name='colors',
            field=models.ManyToManyField(blank=True, to='tonyapp.color'),
        ),
        migrations.AddField(
            model_name='clothing',
            name='sizes',
            field=models.ManyToManyField(blank=True, to='tonyapp.size'),
        ),
        migrations.DeleteModel(
            name='CartItem',
        ),
    ]
