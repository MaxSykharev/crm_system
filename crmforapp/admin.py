from django.contrib import admin

from .models import Company, Employee, Position

"""
register  models
"""


# register  models
@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    filter_horizontal = ('partners',)
    list_display = ['name', 'country', 'email', 'count_employees', 'get_employees', 'created_at','last_changes']


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    filter_horizontal = ('company', 'profession',)
    list_display = ['first_name', 'second_name', 'age', 'knowledge', 'phone_number','email', 'start_work', ]


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    pass
