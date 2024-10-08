# Generated by Django 5.0.7 on 2024-09-08 19:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0008_alter_collection_musics_alter_playlist_musics'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collection',
            name='owner',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_collections', to='music.user'),
        ),
        migrations.AlterField(
            model_name='playlist',
            name='owner',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_playlists', to='music.user'),
        ),
    ]
