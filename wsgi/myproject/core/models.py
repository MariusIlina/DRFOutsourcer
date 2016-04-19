from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class PaymentTypes(models.Model):
    type_name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.type_name


class Currency(models.Model):
    currency_name = models.CharField(max_length=200)
    currency_short_name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.currency_short_name


class Country(models.Model):
    country_name = models.CharField(max_length=200)
    country_code = models.CharField(max_length=200)

    def __unicode__(self):
        return self.country_name 


class Company(models.Model):
    company_name = models.CharField(max_length=200)
    employees_no = models.PositiveSmallIntegerField(default=0)
    description = models.TextField()
    county = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    slug_name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    external_link = models.CharField(max_length=200)
    user = models.ForeignKey(User, null=True, blank=True)

    def __unicode__(self):
        return self.company_name


class Size(models.Model):
    name = models.CharField(max_length=200, null=True, default='')
    short_name = models.CharField(max_length=200, null=True, default='')

    def __unicode__(self):
        return self.name

class Item(models.Model):
    name = models.CharField(max_length=200, null=True, default='')
    size = models.ForeignKey(Size)

    def __unicode__(self):
        return self.name