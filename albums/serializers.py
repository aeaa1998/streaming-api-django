from rest_framework import serializers
from artists.serializers import ArtistSerializer
from tracks.serializers import TrackSerializer
from albums.models import Album 
from tracks.models import Genre

class AlbumSerializer(serializers.ModelSerializer):
	class Meta:
		model = Album
		fields = '__all__'
		#fields = ['id','title']

class AlbumByIdSerializer(serializers.ModelSerializer):
	artist = ArtistSerializer()
	tracks = TrackSerializer(many=True)
	class Meta:
		model = Album
		fields = ['id', 'title', 'price', 'created_at', 'artist', 'tracks']
		

# class AlbumByGenreSerializer(serializers.ModelSerializer):
# 	albums = AlbumSerializer(many=True)
# 	class Meta:
# 		model = Genre
# 		fields = ['id', 'name', 'albums']
		
