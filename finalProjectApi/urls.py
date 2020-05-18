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
router = routers.DefaultRouter()
router.register(r'profiles', profileViews.ProfileViewSet)
urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
    url(r'^api/login/', obtain_jwt_token),
    url(r'^api/register/', profileViews.RegisterView.as_view({'post': 'create'} )),
    url(r'^api/token-refresh/', refresh_jwt_token)
]