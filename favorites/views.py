from rest_framework import viewsets , permissions
from .models import Favorite
from .serializers import FavoritePolymorphicSerializer, FavoritePolymorphicSerializerCreate
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.decorators import action
from profiles.serializers import UserSerializer
from django.core import serializers
import random

class FavoriteViewSet(viewsets.ModelViewSet):
	queryset = Favorite.objects.all()
	serializer_class = FavoritePolymorphicSerializer

	def create(self, request):
		request.data['user'] = request.user.id
		serializer = FavoritePolymorphicSerializerCreate(data=request.data)
		if serializer.is_valid():
			serializer.save()
			favorite = Favorite.objects.get(pk=serializer.data['id'])
			serializer_context = {'request': Request(request._request)}
			return Response(self.serializer_class(favorite, context=serializer_context).data, 200)
			# return Response(data=serializer.data, status=200)
		else:
			return Response(serializer.errors, status=400)

