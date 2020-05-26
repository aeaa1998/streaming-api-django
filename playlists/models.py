from django.db import models
from django.contrib.auth.models import User
from tracks.models import Track

# Create your models here.
class Playlist(models.Model):
	name = models.CharField(max_length=50)
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="playlists")
	created_at = models.DateTimeField(auto_now_add=True, blank=True)
	updated_at = models.DateTimeField(auto_now_add=True, blank=True)
	tracks = models.ManyToManyField(Track, blank=True, related_name="playlist")
	class Meta:
		db_table = 'playlists'
	
	  