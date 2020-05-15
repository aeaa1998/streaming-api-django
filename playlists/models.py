from django.db import models
from profiles.models import Profile

# Create your models here.
class Playlist(models.Model):
	
	name = models.CharField(max_length=50)
	owner_profile = models.ForeignKey(Profile, on_delete= models.CASCADE, default=0)
	
	
	 