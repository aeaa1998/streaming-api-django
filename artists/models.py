from django.db import models

# Create your models here.
class Artist(models.Model):
    name = models.CharField(max_length=200)
    bio = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now_add=True, blank=True)
    class Meta:
            db_table = 'artists'