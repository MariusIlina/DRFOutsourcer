from django.contrib import admin
from .models import Item, Size


# # Register your models here.
# class TodoAdmin(admin.ModelAdmin):
#     list_display = ('propietario', 'todo', 'hecho')
#     exclude = ('propietario',)
#
#     def save_model(self, request, obj, form, change):
#         obj.propietario = request.user
#         obj.save()

admin.site.register(Item)
admin.site.register(Size)
#admin.site.register(Todo)
#admin.site.register(Currencies)