from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from core.api.serializers import ItemSerializer, UserSerializer, SizeSerializer, ItemHyperSerializer, \
    ItemNestedSerializer, CompanySerializer, CountrySerializer
from django.contrib.auth.models import User
from core.models import Item, Size, Company, Country
from django.http import Http404
from rest_framework import status


# Create your views here.


class SizeList(APIView):
    serializer_class = SizeSerializer

    def get(self, request, id=None, format=None):
        if id is not None:
            sizes = get_object_or_404(Size, pk=id)
            many = False
        else:
            sizes = Size.objects.all()
            many = True
        response = self.serializer_class(sizes, many=many)
        return Response(response.data)

sizes_all = SizeList.as_view()


class ItemList(APIView):
    serializer_class = ItemNestedSerializer

    def get(self, request, id=None):
        items = Item.objects.all()
        response = self.serializer_class(items, many=True, context={'request': request})
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

class CountryViewSet(viewsets.ModelViewSet):
    serializer_class = CountrySerializer
    queryset = Country.objects.all()

class CompanyViewSet(viewsets.ModelViewSet):
    serializer_class = CompanySerializer
    queryset = Company.objects.all()

    def create(self, request, *args, **kwargs):
        request.data['user_id'] = request.user.id
        return super(self.__class__, self).create(request, *args, **kwargs)

class SizeViewSet(viewsets.ModelViewSet):
    serializer_class = SizeSerializer
    queryset = Size.objects.all()

class ItemViewSet(viewsets.ModelViewSet):
    serializer_class = ItemSerializer
    queryset = Item.objects.all()

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