from rest_framework import serializers
from tracks.models import Track, Genre, TrackFeatures
from artists.models import Artist
from artists.serializers import ArtistSerializer
from albums.models import Album 

class AlbumByTrackSerializer(serializers.ModelSerializer):
	artist = ArtistSerializer()
	class Meta:
		model = Album
		fields = ['id', 'title', 'price', 'created_at', 'artist']

class TrackSerializer(serializers.ModelSerializer):
	class Meta:
		model = Track
		fields = '__all__'
		

class GenreSerializer(serializers.ModelSerializer):
	class Meta:
		model = Genre
		fields = '__all__'


class TrackFeatureSerializer(serializers.ModelSerializer):
	featured_artist = ArtistSerializer()
	class Meta:
		model = TrackFeatures
		fields = ['featured_artist']

class TrackByIdSerializer(serializers.ModelSerializer):
	album = AlbumByTrackSerializer()
	features = TrackFeatureSerializer(many=True)
	class Meta:
		model = Track
		fields = ['id', 'explicit_lyrics', 'price', 'name','album', 'genre_id', 'features']
		