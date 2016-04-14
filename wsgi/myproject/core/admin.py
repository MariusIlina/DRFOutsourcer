from django.contrib import admin
from .models import Todo, Currencies


# Register your models here.
class TodoAdmin(admin.ModelAdmin):
    list_display = ('propietario', 'todo', 'hecho')

admin.site.register(Todo, TodoAdmin)
admin.site.register(Currencies)