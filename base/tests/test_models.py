from django.test import TestCase
from base.models import Department, Employee
from faker import Faker


fake = Faker(['ru_RU'])
department_depth_level = 5
department_count_for_each_head_office = 3
employee_count = 5


class ModelsTestCase(TestCase):
    def setUp(self):
        # create departments and subdivisions
        Department.objects.create(name=fake.bs(), head_office=None)
        dep = Department.objects.all()
        base_count = dep.count()
        for _ in range(department_depth_level):
            for i in dep:
                for _ in range(department_count_for_each_head_office):
                    Department.objects.create(name=fake.bs(), head_office=i)
                    dep = Department.objects.filter(head_office__isnull=False)
                    dep = dep[ base_count:base_count*department_count_for_each_head_office ]
            base_count *= department_count_for_each_head_office
        # create employees
        for i in Department.objects.all():
            for _ in range(employee_count):
                Employee.objects.create(name=fake.name(), salary=fake.pyint() * 10, date_of_issue=fake.date(), department=i)

    def test_department_count(self):
        dep = Department.objects.all()
        self.assertEqual(dep.count(),  department_count_for_each_head_office ** department_depth_level + 1)

    def test_employee_count(self):
        emp = Employee.objects.all()
        dep = Department.objects.all()
        self.assertEqual(emp.count(), dep.count() * employee_count)