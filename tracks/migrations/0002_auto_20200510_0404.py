# Generated by Django 3.0.6 on 2020-05-10 04:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0003_auto_20200510_0404'),
        ('tracks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='track',
            name='album',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='tracks', to='albums.Album'),
        ),
        migrations.AlterField(
            model_name='track',
            name='genre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='tracks', to='tracks.Genre'),
        ),
    ]
