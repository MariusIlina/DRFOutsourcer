from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer
from rest_framework.serializers import HyperlinkedRelatedField, ValidationError
from core.models import Item, Size, Company, Country
from django.core.validators import validate_email

class CountrySerializer(ModelSerializer):
    class Meta:
        model = Country
        fields = ('country_name', 'country_code')

class CompanySerializer(ModelSerializer):
    class Meta:
        model = Company
        fields = ('id', 'company_name', 'employees_no', 'description', 'country', 'county', 'city',
                  'slug_name', 'email', 'phone', 'external_link', 'user')
        read_only_fields = ('user',)

    def validate(self, data):
        if validate_email(data['email']) is False:
            raise ValidationError("You must provide a valid email")

class SizeSerializer(ModelSerializer):
    class Meta:
        model = Size
        fields = ('id', 'name', 'short_name')


class ItemSerializer(ModelSerializer):
    class Meta:
        model = Item
        fields = ('id', 'name', 'size')

    def validate(self, data):
        if len(data['name']) < 3:
            raise ValidationError("Name must be at least 3 chars long")


class ItemNestedSerializer(ModelSerializer):
    size = SizeSerializer(read_only=True)

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