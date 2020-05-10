from rest_framework import routers, serializers, viewsets
from django.contrib import admin
from django.urls import path
from rest_framework_jwt.views import (
    obtain_jwt_token,
    refresh_jwt_token
)

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^api/login/', obtain_jwt_token),
    url(r'^api/v1/token-refresh/', refresh_jwt_token)
]
