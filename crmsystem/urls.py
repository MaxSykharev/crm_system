from django.contrib import admin
from django.urls import path
from rest_framework import routers

from crmforapp.views import EmployeeViewSet, CompaniesViewSet, PositionsViewSet

urlpatterns = [
    path('admin/', admin.site.urls),
]

"""
urls to all ViewSet 
"""
router = routers.SimpleRouter()
router.register('api/EmployeeList', EmployeeViewSet, basename='employees')
router.register('api/CompaniesList', CompaniesViewSet, basename='companies')
router.register('api/PositionsList', PositionsViewSet, basename='positions')

urlpatterns += router.urls
