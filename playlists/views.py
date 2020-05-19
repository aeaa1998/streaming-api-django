from rest_framework import viewsets , permissions
from .serializers import PlaylistSerializer, PlaylistWithTracksSerializer
from playlists.models import Playlist
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.decorators import action

class PlaylistViewSet(viewsets.ModelViewSet):
	queryset = Playlist.objects.all()
	serializer_class = PlaylistSerializer
	
	def list(self, request):
		playlists = Playlist.objects.filter(user__pk = request.user.id)
		serializer_context = {'request': Request(request._request)}
		return Response(PlaylistWithTracksSerializer(playlists, many=True, context=serializer_context).data)

	@action(detail=False, url_path='add/track/(?P<pk>\d+)', methods=['post'])
	def addTrack(self, request, pk):
		playlist = Playlist.objects.get(pk=pk)
		track = request.data['track']
		playlist.tracks.add(track)
		serializer_context = {'request': Request(request._request)}
		return Response(PlaylistWithTracksSerializer(playlist, context=serializer_context).data)

