from rest_framework.test import APIRequestFactory
from rest_framework.test import APITestCase
from base.api.views import department_list, department_list_by_parent_department


class DepartmentListTestCase(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()

    def test_department_list(self):
        request = self.factory.get('/department/1/')
        response = department_list(request)
        self.assertEqual(response.status_code, 200)

    def test_department_list_by_parent_department(self):
        request = self.factory.get('/department-list/1/')
        response = department_list_by_parent_department(request, department_id=1)
        self.assertEqual(response.status_code, 200)

