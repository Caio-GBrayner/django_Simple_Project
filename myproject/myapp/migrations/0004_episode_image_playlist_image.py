# Generated by Django 5.1.2 on 2024-12-03 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_remove_episode_created_at_remove_episode_updated_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='episode',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='episode_images/'),
        ),
        migrations.AddField(
            model_name='playlist',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='playlist_images/'),
        ),
    ]
