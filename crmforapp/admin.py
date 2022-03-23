from django.contrib import admin

# Register your models here.
from .models import Company, Employee, Position


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['name', 'country', 'get_friends', 'email', 'count_employees', 'get_employees', 'created_at',
                    'last_changes']


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'second_name', 'age', 'get_company', 'get_profession', 'knowledge', 'phone_number',
                    'email', 'start_work', ]


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
