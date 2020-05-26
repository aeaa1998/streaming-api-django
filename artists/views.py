
from rest_framework import viewsets , permissions
from .serializers import ArtistSerializer, ArtistByGenreSerializer, ArtistByIdSerializer
from artists.models import Artist
from tracks.models import Genre
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.decorators import action

class ArtistViewSet(viewsets.ModelViewSet):
	queryset = Artist.objects.all()
	serializer_class = ArtistSerializer
	
	@action(detail=False, url_path='by/genres', methods=['get'])
	def listByGenre(self, request):
		genres = Genre.objects.all()
		firstCat = {
			'id': 0, 'name': 'Todos los artistas', 'artists': self.queryset[:20]
		}
		artists = [firstCat]
		for genre in genres:
			nextCat = {'id': genre.id, 'name': genre.name, 'artists': self.queryset.filter(albums__tracks__genre__pk=genre.id).distinct()[:20]}
			artists.append(nextCat)
		serializer_context = {'request': Request(request._request)}
		return Response(ArtistByGenreSerializer(artists, many=True, context=serializer_context).data, 200)

	def retrieve(self, request, pk):
		artist = self.queryset.get(pk=pk)
		serializer_context = {'request': Request(request._request)}
		return Response(ArtistByIdSerializer(artist, context=serializer_context).data, 200)
