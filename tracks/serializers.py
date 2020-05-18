from rest_framework import serializers

from tracks.models import Track, Genre

class TrackSerializer(serializers.ModelSerializer):
	class Meta:
		model = Track
		fields = '__all__'
		

class GenreSerializer(serializers.ModelSerializer):
	class Meta:
		model = Genre
		fields = '__all__'
		