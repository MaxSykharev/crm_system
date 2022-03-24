from django.contrib import admin
from django.urls import path
from rest_framework import routers

from crmforapp.views import EmployeeViewSet, CompaniesViewSet, PositionsViewSet

urlpatterns = [
    path('admin/', admin.site.urls),
]

router = routers.SimpleRouter()
router.register('api/EmployeeList', EmployeeViewSet)
router.register('api/CompaniesList', CompaniesViewSet)
router.register('api/PositionsList', PositionsViewSet)
"""
urls to all ViewSet 
"""

urlpatterns += router.urls
