from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from core.api.serializers import UserSerializer
from django.contrib.auth.models import User

# Create your views here.

class HolaMundo(APIView):

    def get(self, request, nombre, format=None):
        return Response({'mensaje':'Hola ' + nombre + ' en el mundo de Django Rest Framework'})

hola_mundo = HolaMundo.as_view()

class Usuario(APIView):
    serializer_class = UserSerializer

    def get(self, request, id=None, format=None):
        if id != None:
            users = get_object_or_404(User, pk=id)
            many = False
        else:
            users = User.objects.all()
            many = True
        response = self.serializer_class(users, many=many)
        return Response(response.data)

usuarios = Usuario.as_view()