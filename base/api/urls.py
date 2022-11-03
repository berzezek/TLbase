from .views import department_list, department_list_by_parent_department, department_detail, employee_list, employee_detail
from django.urls import path

urlpatterns = [
    path('department/', department_list),
    path('department/<int:department_id>/', department_detail),
    path('department-list/<int:department_id>/', department_list_by_parent_department),
    path('department/<int:department_id>/employee/', employee_list),
    path('employee/<int:employee_id>/', employee_detail),
]