from rest_framework import serializers
from django_countries.serializers import CountryFieldMixin

from .models import Employee, Company, Position


class EmployeeSerializer(CountryFieldMixin, serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('__all__')


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('__all__')

class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = ('__all__')
