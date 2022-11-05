from django.test import TestCase, Client
from django.contrib.auth.models import User
from base.models import Department, Employee


class AdminTestPanel(TestCase):
    def setUp(self):
        d = Department.objects.create(name="test")
        Employee.objects.create(name="test", salary=100, date_of_issue="2020-01-01", department=d)

    def create_user(self):
        self.username = "test_admin"
        self.password = User.objects.make_random_password()
        user, created = User.objects.get_or_create(username=self.username)
        user.set_password(self.password)
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        user.save()
        self.user = user

    def test_spider_admin(self):
        self.create_user()
        client = Client()
        client.login(username=self.username, password=self.password)
        admin_pages = [
            "/admin/",

            "/admin/base/department/",
            "/admin/base/department/add/",
            f"/admin/base/department/add/?department={Department.objects.first().id}",
            f"/admin/base/department/{Department.objects.first().id}/change/",
            f"/admin/base/department/{Department.objects.first().id}/delete/",

            "/admin/base/employee/",
            "/admin/base/employee/add/",
            f"/admin/base/employee/add/?department={Department.objects.first().id}",
            f"/admin/base/employee/{Employee.objects.first().id}/change/",
            f"/admin/base/employee/{Employee.objects.first().id}/delete/",
        ]
        for page in admin_pages:
            resp = client.get(page)
            assert resp.status_code == 200
            assert "<!DOCTYPE html" in resp.content.decode("utf-8")
