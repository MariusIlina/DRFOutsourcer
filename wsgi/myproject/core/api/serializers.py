from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer
from core.models import Todo

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

class TodoSerializer(ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id', 'fecha_creado', 'fecha_finalizado', 'todo', 'hecho', 'propietario')
        read_only_fields = ('propietario',)