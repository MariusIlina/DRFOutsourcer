from core.models import *
from core.seed import Seed

for u in Seed.users:
    user = User()
    user.id = u['id']
    user.set_password(u['password'])
    user.username = u['username']
    user.email = u['email']
    user.save()

for c in Seed.countries:
    country = Country()
    country.id = c['id']
    country.country_name = c['country_name']
    country.country_code = c['country_code']
    country.save()

for t in Seed.time_units:
    time_unit = TimeUnit()
    time_unit.id = t['id']
    time_unit.unit_name = t['unit_name']
    time_unit.save()

for c in Seed.currencies:
    currency = Currency()
    currency.id = c['id']
    currency.currency_name = c['currency_name']
    currency.currency_short_name = c['currency_short_name']
    currency.save()

for p in Seed.payment_types:
    payment_type = PaymentTypes()
    payment_type.id = p['id']
    payment_type.type_name = p['type_name']
    payment_type.save()

for c in Seed.categories:
    category = Category()
    category.id = c['id']
    category.category_name = c['category_name']
    category.save()

Seed.users
Seed.countries
Seed.time_units
Seed.currencies
Seed.payment_types
Seed.categories
