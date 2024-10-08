# Generated by Django 5.0.7 on 2024-09-08 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0007_user_is_creator'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collection',
            name='musics',
            field=models.ManyToManyField(blank=True, related_name='music_collection', to='music.music'),
        ),
        migrations.AlterField(
            model_name='playlist',
            name='musics',
            field=models.ManyToManyField(blank=True, related_name='music_playlists', to='music.music'),
        ),
    ]
