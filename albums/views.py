from rest_framework import viewsets , permissions
from .serializers import AlbumSerializer
from albums.models import Album

class AlbumViewSet(viewsets.ModelViewSet):
	queryset = Album.objects.all()
	serializer_class = AlbumSerializer
	permission_classes= [
	  permissions.AllowAny
	]
	

