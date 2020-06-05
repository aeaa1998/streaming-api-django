from django.db import models
from albums.models import Album
from artists.models import Artist


# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now_add=True, blank=True)
    class Meta:
            db_table = 'genres'

class Track(models.Model):
    name = models.CharField(max_length=200)
    album = models.ForeignKey(Album, on_delete=models.PROTECT, related_name="tracks")
    genre = models.ForeignKey(Genre, on_delete=models.PROTECT, related_name="tracks")
    price = models.FloatField(default=0.99)
    seconds = models.IntegerField(default=180)
    explicit_lyrics = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now_add=True, blank=True)
    class Meta:
            db_table = 'tracks'

class TrackFeatures(models.Model):
    track = models.ForeignKey(Track, on_delete=models.PROTECT, related_name="features")
    featured_artist = models.ForeignKey(Artist, on_delete=models.PROTECT, related_name="features")
    class Meta:
        db_table = 'track_features'