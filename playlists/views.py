from rest_framework import viewsets , permissions
from .serializers import PlaylistSerializer, PlaylistWithTracksSerializer
from playlists.models import Playlist
from rest_framework.response import Response
from guardian.shortcuts import assign_perm
from rest_framework.request import Request
from rest_framework.decorators import action

class PlaylistViewSet(viewsets.ModelViewSet):
	queryset = Playlist.objects.all()
	serializer_class = PlaylistSerializer
	
	def list(self, request):
		playlists = Playlist.objects.filter(user__pk = request.user.id)
		serializer_context = {'request': Request(request._request)}
		return Response(self.serializer_class(playlists, many=True, context=serializer_context).data)

	def destroy(self, request, *args, **kwargs):
		instance = self.get_object()
		if request.user.has_perm('delete_playlist', instance):
			return super().destroy(self, request, *args, **kwargs)
		else:
			return Response("Illegal action", 400)

	def retrieve(self, request, pk):
		playlists = Playlist.objects.get(user__pk = request.user.id, pk=pk)
		serializer_context = {'request': Request(request._request)}
		return Response(PlaylistWithTracksSerializer(playlists, context=serializer_context).data)


	def retrieveTracks(self, request, pk):
		playlists = Playlist.objects.get(user__pk = request.user.id, pk=pk)
		serializer_context = {'request': Request(request._request)}
		return Response(PlaylistWithTracksSerializer(playlists, context=serializer_context).data)

	def create(self, request): 
		request.data['user'] = request.user.id
		serializer = PlaylistSerializer(data=request.data) 
		if serializer.is_valid():
			serializer.save()
			playlist = Playlist.objects.get(pk=serializer.data['id'])
			assign_perm('change_playlist', request.user, playlist)
			assign_perm('delete_playlist', request.user, playlist)
			serializer_context = {'request': Request(request._request)}
			return Response(self.serializer_class(playlist, context=serializer_context).data, 200)
			# return Response(data=serializer.data, status=200)
		else:
			return Response(serializer.errors, status=400)

	@action(detail=False, url_path='add/track/(?P<pk>\d+)', methods=['post'])
	def addTrack(self, request, pk):
		playlist = Playlist.objects.get(pk=pk)
		if request.user.has_perm('change_playlist', playlist):
			track = request.data['track']
			playlist.tracks.add(track)
			return Response("Successfully added track", 200)
		return Response("Illegal action", 400)

	@action(detail=False, url_path='delete/track/(?P<pk>\d+)', methods=['delete'])
	def deleteTrack(self, request, pk):
		playlist = Playlist.objects.get(pk=pk)
		if request.user.has_perm('change_playlist', playlist):
			track = request.data['track']
			playlist.tracks.remove(track)
			return Response("Successfully deleted track", 200)
		return Response("Illegal action", 400)

