
from rest_framework import viewsets , permissions
from .serializers import ArtistSerializer
from artists.models import Artist

class ArtistViewSet(viewsets.ModelViewSet):
	queryset = Artist.objects.all()
	serializer_class = ArtistSerializer
	permission_classes= [
	  permissions.AllowAny
	]
	

