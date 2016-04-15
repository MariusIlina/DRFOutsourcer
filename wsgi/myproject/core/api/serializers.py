from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer, HyperlinkedRelatedField
from core.models import Item, Size

class SizeSerializer(ModelSerializer):
    class Meta:
        model = Size
        fields = ('id', 'name', 'short_name')


class ItemSerializer(ModelSerializer):
    class Meta:
        model = Item
        fields = ('id', 'name', 'size')


class ItemHyperSerializer(HyperlinkedModelSerializer):

    size = HyperlinkedRelatedField(
        view_name = 'sizeintro',
        lookup_field = 'id',
        many = False,
        read_only = True
    )

    class Meta:
        model = Item
        fields = ('id', 'name', 'size')



class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

# class TodoSerializer(ModelSerializer):
#     class Meta:
#         model = Todo
#         fields = ('id', 'fecha_creado', 'fecha_finalizado', 'todo', 'hecho', 'propietario')
#         read_only_fields = ('propietario',)
#
# class CurrencySerializer(ModelSerializer):
#     class Meta:
#         model = Currencies
#         fields = ('id', 'currency_name', 'short_name')