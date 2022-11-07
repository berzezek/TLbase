from base.api.views import department_list, department_list_by_parent_department, department_detail, employee_list, employee_detail
from django.urls import reverse, resolve
from django.test import SimpleTestCase


class UrlsTestCase(SimpleTestCase):
    def test_list_url(self):
        url_department_list = reverse('department_list')
        url_department_list_by_parent_department = reverse('department_list_by_parent_department', args=[1])
        url_department_detail = reverse('department_detail', args=[1])
        url_employee_list = reverse('employee_list', args=[1])
        url_employee_detail = reverse('employee_detail', args=[1])

        self.assertEqual(resolve(url_department_list).func, department_list)
        self.assertEqual(resolve(url_department_list_by_parent_department).func, department_list_by_parent_department)
        self.assertEqual(resolve(url_department_detail).func, department_detail)
        self.assertEqual(resolve(url_employee_list).func, employee_list)
        self.assertEqual(resolve(url_employee_detail).func, employee_detail)