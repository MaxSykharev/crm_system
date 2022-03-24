from django.contrib import admin
from django.urls import path
from rest_framework import routers

from crmforapp.views import EmployeeViewSet, CompaniesViewSet

urlpatterns = [
    path('admin/', admin.site.urls),
]

router = routers.SimpleRouter()
router.register('api/v1/EmployeeList', EmployeeViewSet)
router.register('api/v1/CompaniesList', CompaniesViewSet)
urlpatterns += router.urls
