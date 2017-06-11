from django.contrib import admin
from .models import Company, Country, Category, PaymentTypes, Currency, TimeUnit, Project, Bid, Recommendation, Comment


# Register your models here.

admin.site.register(Country)
admin.site.register(Company)
admin.site.register(Category)
admin.site.register(PaymentTypes)
admin.site.register(Currency)
admin.site.register(TimeUnit)
admin.site.register(Project)
admin.site.register(Bid)
admin.site.register(Comment)
admin.site.register(Recommendation)
