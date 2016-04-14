from django.contrib import admin
from .models import Todo, Currencies


# Register your models here.
admin.site.register(Todo, Currencies)