from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from core.api.serializers import UserSerializer, TodoSerializer
from django.contrib.auth.models import User
from core.models import Todo

# Create your views here.

class TodoView(APIView):
    serializer_class = TodoSerializer

    def get(self, request, id=None, format=None):
        todos = Todo.objects.all()
        response = self.serializer_class(todos, many=True)
        return Response(response.data)

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            return Response(serializer)
        else:
            return Response(serializer.errors)

to_do = TodoView.as_view()



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