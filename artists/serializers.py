from rest_framework import serializers
from artists.models import Artist 
from tracks.models import Genre, Track
from albums.models import Album

class TrackSerializer(serializers.ModelSerializer):
	class Meta:
		model = Track
		fields = '__all__'
class ArtistSerializer(serializers.ModelSerializer):

	class Meta:
		model = Artist
		fields = '__all__'


class AlbumByIdSerializer(serializers.ModelSerializer):
	tracks = TrackSerializer(many=True)
	class Meta:
		model = Album
		fields = ['id', 'title', 'price', 'created_at', 'tracks']

class ArtistByIdSerializer(serializers.ModelSerializer):
	albums = AlbumByIdSerializer(many=True)
	class Meta:
		model = Artist
		fields = ['id', 'name', 'bio', 'albums']
		
class ArtistByGenreSerializer(serializers.ModelSerializer):
	artists = ArtistSerializer(many=True)
	class Meta:
		model = Genre
		fields = ['id', 'name', 'artists']
		
