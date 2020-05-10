# Generated by Django 3.0.6 on 2020-05-10 04:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('artists', '0001_initial'),
        ('albums', '0002_album_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='artist',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='albums', to='artists.Artist'),
        ),
    ]
