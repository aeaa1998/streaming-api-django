from rest_framework import viewsets , permissions
from .serializers import PlaylistSerializer
from playlists.models import Playlist

class PlaylistViewSet(viewsets.ModelViewSet):
	queryset = Playlist.objects.all()
	serializer_class = PlaylistSerializer
	permission_classes= [
	  permissions.AllowAny
	]
	

