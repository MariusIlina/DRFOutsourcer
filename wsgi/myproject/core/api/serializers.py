from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer #HyperlinkedModelSerializer
from rest_framework.serializers import ValidationError #HyperlinkedRelatedField
from core.models import Company, Country
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
            raise ValidationError()
        return data