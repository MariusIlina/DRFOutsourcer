from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from core.api.serializers import ItemSerializer, UserSerializer
from django.contrib.auth.models import User
from core.models import Item
from django.http import Http404
from rest_framework import status


# Create your views here.

class ItemList(APIView):

    def get(self, request, id=None):
        items = Item.objects.all()
        response = ItemSerializer(items, many=True)
        return Response(response.data)

items = ItemList.as_view()


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

# class CurrencyView(APIView):
#
#     def get(self, request, id=None, format=None):
#         curr = Currencies.objects.all()
#         response = CurrencySerializer(curr, many=True)
#         return Response(response.data)
#
#     def post(self, request, format=None):
#         serializer = CurrencySerializer(data=request.data)
#
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
# valuta = CurrencyView.as_view()
#
#
#
# class TodoView(APIView):
#
#     def get(self, request, id=None, format=None):
#         todos = Todo.objects.all()
#         response = TodoSerializer(todos, many=True)
#         return Response(response.data)
#
#     def post(self, request, format=None):
#         serializer = TodoSerializer(data=request.data)
#
#         if serializer.is_valid():
#             serializer.propietario = request.user
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
# to_do = TodoView.as_view()
#
#
#
# class HolaMundo(APIView):
#
#     def get(self, request, nombre, format=None):
#         return Response({'mensaje':'Hola ' + nombre + ' en el mundo de Django Rest Framework'})
#
# hola_mundo = HolaMundo.as_view()
#
#
#