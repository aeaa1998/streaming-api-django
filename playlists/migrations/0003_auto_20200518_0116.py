# Generated by Django 3.0.6 on 2020-05-18 01:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('playlists', '0002_playlist_owner_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='playlist',
            name='owner_profile',
        ),
        migrations.AddField(
            model_name='playlist',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='playlists', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterModelTable(
            name='playlist',
            table='playlists',
        ),
    ]
