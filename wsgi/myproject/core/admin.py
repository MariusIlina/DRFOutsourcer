from django.contrib import admin
from .models import Company, Country, PaymentTypes, Currency, TimeUnit, Project, Bid


# Register your models here.

admin.site.register(Country)
admin.site.register(Company)
admin.site.register(PaymentTypes)
admin.site.register(Currency)
admin.site.register(TimeUnit)
admin.site.register(Project)
admin.site.register(Bid)
