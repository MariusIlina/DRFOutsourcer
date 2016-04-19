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


class TimeUnit(models.Model):
    unit_name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.unit_name


class Company(models.Model):
    company_name = models.CharField(max_length=200)
    employees_no = models.PositiveSmallIntegerField(default=0)
    description = models.TextField()
    country = models.ForeignKey(Country, null=True, blank=True)
    county = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    slug_name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    external_link = models.CharField(max_length=200)
    user = models.ForeignKey(User, null=True, blank=True)

    def __unicode__(self):
        return self.company_name


class Project(models.Model):
    project_name = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    by_company = models.ForeignKey(Company, null=True, blank=True)
    approximate_duration = models.CharField(max_length=200, null=True, blank=True)
    approximate_duration_time_unit = models.ForeignKey(TimeUnit, null=True, blank=True)
    description = models.TextField()
    slug_name = models.CharField(max_length=200, null=True)
    required_techs = models.TextField(null=True)
    approximate_hours_per_week = models.IntegerField(default=0)
    payment_type = models.ForeignKey(PaymentTypes, null=True, blank=True)
    payment_amount = models.IntegerField(default=0)
    currency = models.ForeignKey(Currency, null=True)

    def __unicode__(self):
        return self.project_name
