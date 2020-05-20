from rest_framework import serializers
from tracks.serializers import TrackListSerializer
from playlists.models import Playlist 

class PlaylistSerializer(serializers.ModelSerializer):

	class Meta:
		model = Playlist
		fields = '__all__'

class PlaylistWithTracksSerializer(serializers.ModelSerializer):
	tracks = TrackListSerializer(many=True)
	class Meta:
		model = Playlist
		fields = ['id','user','name', 'tracks', 'created_at']
		