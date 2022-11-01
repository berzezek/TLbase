from .views import category_list, category_list_by_parent_category, category_detail, employee_list, employee_detail
from django.urls import path

urlpatterns = [
    path('category/', category_list),
    path('category/<int:category_id>/', category_detail),
    path('category-list/<int:category_id>/', category_list_by_parent_category),
    path('category/<int:category_id>/employee/', employee_list),
    path('employee/<int:employee_id>/', employee_detail),
]