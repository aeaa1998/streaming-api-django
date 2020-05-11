from django.shortcuts import render
from profiles.models import Profile
from django.db import IntegrityError
import json
from rest_framework.request import Request
from django.contrib.auth.models import User
from profiles.serializers import ProfileSerilializer
from rest_framework.response import Response
from rest_framework.decorators import action
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework import routers, serializers, viewsets
# Create your views here.
class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerilializer
    

    def list(self, request):
        try:
            profile =  Profile.objects.get(user__pk=request.user.id)
            serializer_context = {'request': Request(request._request)}
            return Response(ProfileSerilializer(profile, context=serializer_context).data)
        except (Exception) as e:
            return Response("user_does_not_have_profile", 404)


class RegisterView(viewsets.ModelViewSet):
    permission_classes = ()
    queryset = Profile.objects.all()
    serializer_class = ProfileSerilializer
    permission_classes = ()

    def create(self, request):
        try:
            first_name = request.data['first_name']
            
            email = request.data['email']
            username = request.data['username']
            password = request.data['password']
            user = User.objects.create_user(username, email, password)
            user.first_name = first_name
            user.save()
            profile = Profile(user=User.objects.get(username=username))
            profile.save()
            serializer_context = {'request': Request(request._request)}
            return Response(ProfileSerilializer(profile, context=serializer_context).data)
        except (IntegrityError) as e:
            if (str(e).find("username") > -1):
                return Response({"errorMessage" : "Ese usuario ya ha sido tomado"}, 412)
            else:
                return Response({"errorMessage" : "Ese correo ya ha sido tomado"}, 412)
        except (KeyError) as e:
            return HttpResponse(json.dumps({"errorMessage" : "missing_fields"}), 412)
        except (User.DoesNotExist):
            return HttpResponse(json.dumps({"errorMessage" : "Error al crear el ususario"}), 404)
        except (Exception) as e:
            return Response({"errorMessage" : "Ese usuario ya ha sido tomado"}, 412)