from django.contrib import admin
from .models import Company
from .models import Country
from .models import Category
from .models import PaymentTypes
from .models import Currency
from .models import TimeUnit
from .models import Project
from .models import Bid
from .models import Recommendation
from .models import Comment

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
