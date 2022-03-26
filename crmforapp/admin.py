from django.contrib import admin

from .models import Company, Employee, Position

"""
register  models
"""


# register  models
@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['name', 'country', 'get_partners', 'email', 'count_employees', 'get_employees', 'created_at',
                    'last_changes']


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['user', 'first_name', 'second_name', 'age', 'get_company', 'get_profession', 'knowledge',
                    'phone_number',
                    'email', 'start_work', ]


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    pass
