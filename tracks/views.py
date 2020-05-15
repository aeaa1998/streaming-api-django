from rest_framework import viewsets , permissions
from .serializers import TrackSerializer ,GenreSerializer
from tracks.models import Track, Genre

class TrackViewSet(viewsets.ModelViewSet):
	queryset = Track.objects.all()
	serializer_class = TrackSerializer
	permission_classes= [
	  permissions.AllowAny
	]
	
class GenreViewSet(viewsets.ModelViewSet):
	queryset = Genre.objects.all()
	serializer_class = GenreSerializer
	permission_classes= [
	  permissions.AllowAny
	]
	
