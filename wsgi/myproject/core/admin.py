from django.contrib import admin
from .models import Company, Country


# Register your models here.

admin.site.register(Country)
admin.site.register(Company)
