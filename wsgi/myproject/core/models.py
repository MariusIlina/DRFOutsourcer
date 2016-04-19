from django.db import models
from django.contrib.auth.models import User

# Create your models here.

"""
Types of payments that a company can require. Eg. Hourly, Monthly etc.
"""
class PaymentTypes(models.Model):
    type_name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.type_name


"""
Types of available currencies
"""
class Currency(models.Model):
    currency_name = models.CharField(max_length=200)
    currency_short_name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.currency_short_name


"""
Units of measure for projects duration. Eg. Weeks, Months, Years
"""
class TimeUnit(models.Model):
    unit_name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.unit_name


"""
A set of available countries for company location
"""
class Country(models.Model):
    country_name = models.CharField(max_length=200)
    country_code = models.CharField(max_length=200)

    def __unicode__(self):
        return self.country_name


"""
Defines the structure of a Company entity in Outsourcer
"""
class Company(models.Model):
    company_name = models.CharField(max_length=200)
    registration_number = models.CharField(max_length=200, null=True, blank=True)
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


"""
Defines the structure of a Project entity in Outsourcer
"""
class Project(models.Model):
    project_name = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now=True)
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


"""
Bids are the mean by which a company makes an fee offer to take a project
"""
class Bid(models.Model):
    payment_type = models.ForeignKey(PaymentTypes, null=True, blank=True)
    payment_amount = models.IntegerField(default=0)
    currency = models.ForeignKey(Currency, null=True)
    project = models.ForeignKey(Project, null=True)
