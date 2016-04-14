from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.

class HolaMundo(APIView):
    def get(self, request, nombre, format=None):
        return Response({'mensaje':'Hola ' + nombre + ' en el mundo de Django Rest Framework'})

hola_mundo = HolaMundo.as_view()