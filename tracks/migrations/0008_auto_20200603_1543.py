# Generated by Django 3.0.4 on 2020-06-03 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracks', '0007_remove_track_playlists'),
    ]

    operations = [
        migrations.AlterField(
            model_name='track',
            name='explicit_lyrics',
            field=models.IntegerField(default=0),
        ),
    ]