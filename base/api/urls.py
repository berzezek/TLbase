from .views import category_list, category_detail, employee_list, employee_detail
from django.urls import path

urlpatterns = [
    path('category/', category_list),
    path('category/<int:category_id>/', category_detail),
    path('category/<int:category_id>/employee/', employee_list),
    path('employee/<int:employee_id>/', employee_detail),
]