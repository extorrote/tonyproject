# Generated by Django 5.0.7 on 2024-11-27 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('time', models.TimeField(blank=True, null=True)),
                ('venue_name', models.CharField(blank=True, max_length=200, null=True)),
                ('venue_address', models.CharField(blank=True, max_length=300, null=True)),
                ('ticket_link', models.URLField(blank=True, max_length=500, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('duration', models.CharField(blank=True, max_length=100, null=True)),
                ('special_notes', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='event_images/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('picture', models.ImageField(upload_to='posts_pictures/')),
            ],
        ),
        migrations.CreateModel(
            name='Music',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='music_images/')),
                ('description', models.TextField(blank=True, null=True)),
                ('dropbox_link', models.URLField(blank=True, max_length=1000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post_index',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('picture', models.ImageField(upload_to='posts_pictures/')),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('file', models.FileField(upload_to='songs/')),
                ('background_image', models.ImageField(blank=True, null=True, upload_to='song_images/')),
            ],
        ),
        migrations.CreateModel(
            name='Videos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='music_images/')),
                ('description', models.TextField(blank=True, null=True)),
                ('dropbox_link', models.URLField(blank=True, max_length=1000, null=True)),
                ('youtube_link', models.TextField(blank=True, default='', null=True)),
            ],
        ),
    ]