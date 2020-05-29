from rest_framework import viewsets , permissions
#from .serializers import AlbumSerializer
from artists.serializers import AlbumByIdSerializer , AlbumByGenreSerializer , AlbumSerializer
from albums.models import Album
from tracks.models import Genre
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.decorators import action


class AlbumViewSet(viewsets.ModelViewSet):
	queryset = Album.objects.all()
	serializer_class = AlbumSerializer
	# permission_classes= [
	#   permissions.AllowAny
	# ]


	@action(detail=False, url_path='by/genres', methods=['get'])
	def listByGenre(self, request):
		genres = Genre.objects.all()
		firstCat = {
			'id': 0, 'name': 'Todos los ', 'albums': self.queryset[:20]
		}
		albums = [firstCat]
		for genre in genres:
			# nextCat = {'id': genre.id, 'name': genre.name, 'artists': self.queryset.filter(albums__tracks__genre__pk=genre.id).distinct()[:20]}
			nextCat = {'id': genre.id, 'name': genre.name, 'albums': self.queryset.filter(tracks__genre__pk=genre.id).distinct()[:20]}
			albums.append(nextCat)
		serializer_context = {'request': Request(request._request)}
		return Response(AlbumByGenreSerializer(albums, many=True, context=serializer_context).data, 200)

	def retrieve(self, request, pk):
		album = self.queryset.get(pk=pk)
		serializer_context = {'request': Request(request._request)}
		return Response(AlbumByIdSerializer(album, context=serializer_context).data, 200)

	

