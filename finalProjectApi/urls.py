from rest_framework import routers, serializers, viewsets
from django.contrib import admin
from django.urls import path
from django.urls import include, path
from django.conf.urls import url, include as inc

from profiles import views as profileViews
from rest_framework import routers, serializers, viewsets
router = routers.DefaultRouter()
from rest_framework_jwt.views import (
    obtain_jwt_token,
    refresh_jwt_token
)


from albums.views import AlbumViewSet
from playlists.views import PlaylistViewSet
from tracks.views import TrackViewSet
from favorites.views import FavoriteViewSet
from profiles.views import ProfileViewSet
from artists.views import ArtistViewSet
from tracks.views import GenreViewSet

router = routers.DefaultRouter()
router.register(r'profiles', profileViews.ProfileViewSet)

router.register(r'albums',AlbumViewSet)
router.register(r'playlists',PlaylistViewSet)
router.register(r'tracks',TrackViewSet)
router.register(r'favorites',FavoriteViewSet)
router.register(r'profiles',ProfileViewSet)
router.register(r'artists',ArtistViewSet)
router.register(r'genres',GenreViewSet)
urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
    url(r'^api/login/', obtain_jwt_token),
    url(r'^api/register/', profileViews.RegisterView.as_view({'post': 'create'} )),
    url(r'^api/token-refresh/', refresh_jwt_token)
]
