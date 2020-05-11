from django.db import models
from artists.models import Artist
# Create your models here.
class Album(models.Model):
    title = models.CharField(max_length=200)
    artist = models.ForeignKey(Artist, on_delete=models.PROTECT, related_name="albums")
    price = models.FloatField(default=9.99)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now_add=True, blank=True)
    class Meta:
        db_table = 'albums'