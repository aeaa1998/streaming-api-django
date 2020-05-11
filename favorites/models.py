from django.db import models
from polymorphic.models import PolymorphicModel
from django.contrib.auth.models import User
from artists.models import Artist
from albums.models import Album
from tracks.models import Track
# Create your models here.

class Favorite(PolymorphicModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="favorites")
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now_add=True, blank=True)
    class Meta:
            db_table = 'favorites'

class ArtistFavorite(Favorite):
    artist = models.ForeignKey(Artist, on_delete=models.PROTECT)
    class Meta:
        db_table = 'favorite_artists'

class AlbumFavorite(Favorite):
    album = models.ForeignKey(Album, on_delete=models.PROTECT)
    class Meta:
        db_table = 'favorite_albums'

class TrackFavorite(Favorite):
    track = models.ForeignKey(Track, on_delete=models.PROTECT)
    class Meta:
        db_table = 'favorite_tracks'

