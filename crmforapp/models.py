from django.db import models
from django_countries.fields import CountryField

from .choices import LEVEL


class Position(models.Model):
    """
    represents a position in the company
    """
    name = models.CharField(max_length=30, blank=False, unique=True)
    description = models.TextField(blank=False)

    def __str__(self):
        return self.name


class Company(models.Model):
    """
    represents a company
    """
    created_at = models.DateTimeField(auto_now_add=True)
    last_changes = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=100, unique=True)
    country = CountryField(null=True)
    email = models.EmailField(max_length=100, unique=True)
    partners = models.ManyToManyField('self', blank=True, symmetrical=False)

    @property
    def get_partners(self):
        return list(self.partners.all())


    @property
    def get_employees(self):
        return list(self.employees.all())

    @property
    def count_employees(self):
        return self.employees.count

    def __str__(self):
        return self.name


class Employee(models.Model):
    """
    represents a Employee
    """
    start_work = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=30)
    second_name = models.CharField(max_length=30)
    age = models.IntegerField(default=0)
    skills = models.TextField(max_length=100)
    languages = models.TextField(max_length=100)
    company = models.ManyToManyField(Company, related_name="employees")
    profession = models.ManyToManyField(Position, related_name="employees")
    knowledge = models.PositiveSmallIntegerField('knowledge', choices=LEVEL)
    phone_number = models.CharField(max_length=20, unique=True)
    email = models.EmailField(max_length=100, unique=True)

    @property
    def get_company(self):
        return list(self.company.all())

    @property
    def get_profession(self):
        return list(self.profession.all())

    def __str__(self):
        return self.first_name
