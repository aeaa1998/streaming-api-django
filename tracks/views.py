from rest_framework import viewsets , permissions
from .serializers import TrackSerializer ,GenreSerializer, TrackByIdSerializer, TrackListSerializer
from tracks.models import Track, Genre
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.decorators import action
from django.core import serializers
import random

class TrackViewSet(viewsets.ModelViewSet):
	queryset = Track.objects.all()
	serializer_class = TrackSerializer

	def list(self, request):
		numberTracks =  Track.objects.all().count()
		rand_entities = random.sample(range(numberTracks), 20)
		tracks =  Track.objects.filter(pk__in=rand_entities)
		serializer_context = {'request': Request(request._request)}
		return Response(TrackSerializer(tracks, many= True,context=serializer_context).data)

	@action(detail=False, url_path='list', methods=['get'])
	def listTracksWithDetail(self, request):
		numberTracks =  Track.objects.all().count()
		rand_entities = random.sample(range(numberTracks), 20)
		tracks =  Track.objects.filter(pk__in=rand_entities)
		serializer_context = {'request': Request(request._request)}
		return Response(TrackListSerializer(tracks, many= True,context=serializer_context).data)

	def retrieve(self, request, pk):
		track =  Track.objects.get(pk=pk)
		serializer_context = {'request': Request(request._request)}
		return Response(TrackByIdSerializer(track,context=serializer_context).data)

	@action(detail=False, url_path='genre/(?P<pk>\d+)', methods=['get'])
	def retrieveByGenreId(self, request, pk):
		tracks =  Track.objects.filter(genre__pk=pk)
		serializer_context = {'request': Request(request._request)}
		return Response(TrackByIdSerializer(tracks, many=True, context=serializer_context).data)
	
class GenreViewSet(viewsets.ModelViewSet):
	queryset = Genre.objects.all()
	serializer_class = GenreSerializer
	
