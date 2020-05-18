from django.db import models
from django.contrib.auth.models import User
from profiles.models import Profile

# Create your models here.
class Playlist(models.Model):
	name = models.CharField(max_length=50)
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="playlists")
	created_at = models.DateTimeField(auto_now_add=True, blank=True)
	updated_at = models.DateTimeField(auto_now_add=True, blank=True)
	class Meta:
		db_table = 'playlists'
	
	
	 