from profiles.models import Profile
from rest_framework import serializers
from django.contrib.auth.models import User
from favorites.models import Favorite, ArtistFavorite, AlbumFavorite, TrackFavorite
from artists.serializers import ArtistSerializer
from tracks.serializers import TrackListSerializer
from profiles.serializers import UserSerializer
from rest_polymorphic.serializers import PolymorphicSerializer
from albums.serializers import AlbumSerializer

class FavoriteSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Favorite
        fields = ['user']


class ArtistFavoriteSerializer(serializers.ModelSerializer):
    artist = ArtistSerializer()
    user = UserSerializer()
    class Meta:
        model = ArtistFavorite
        fields = ['id','artist', 'user']


class AlbumFavoriteSerializer(serializers.ModelSerializer):
    album = AlbumSerializer()
    user = UserSerializer()
    class Meta:
        model = AlbumFavorite
        fields = ['id','album', 'user']

class TrackFavoriteSerializer(serializers.ModelSerializer):
    track = TrackListSerializer()
    user = UserSerializer()
    class Meta:
        model = TrackFavorite
        fields = ['id','track', 'user']

class TrackFavoriteSerializerCreate(serializers.ModelSerializer):
    class Meta:
        model = TrackFavorite
        fields = ['id', 'track', 'user']

class AlbumFavoriteSerializerCreate(serializers.ModelSerializer):
    class Meta:
        model = AlbumFavorite
        fields = ['id', 'album', 'user']

class ArtistFavoriteSerializerCreate(serializers.ModelSerializer):
    class Meta:
        model = ArtistFavorite
        fields = ['id', 'artist', 'user']

class FavoritePolymorphicSerializer(PolymorphicSerializer):
    model_serializer_mapping = {
        TrackFavorite: TrackFavoriteSerializer,
        AlbumFavorite: AlbumFavoriteSerializer,
        ArtistFavorite: ArtistFavoriteSerializer
    }

class FavoritePolymorphicSerializerCreate(PolymorphicSerializer):
    model_serializer_mapping = {
        TrackFavorite: TrackFavoriteSerializerCreate,
        AlbumFavorite: AlbumFavoriteSerializerCreate,
        ArtistFavorite: ArtistFavoriteSerializerCreate
    }



