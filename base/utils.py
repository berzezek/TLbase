from .models import Department, Employee
from random import randint


def create_tl_base(department_depth_level=5, max_division=3, employee_count=201):
    from faker import Faker
    fake = Faker(['ru_RU'])
    # create departments
    base_dep_count = randint(1, max_division)
    start = 0
    stop = base_dep_count
    for _ in range(base_dep_count):
        Department.objects.create(name=fake.bs())

    # create divisions
    for _ in range(department_depth_level):
        dep = Department.objects.all()[start:stop]
        for i in dep:
            division_dep_count = randint(1, max_division)
            start += division_dep_count
            stop += division_dep_count
            for _ in range(division_dep_count):
                Department.objects.create(name=fake.bs(), head_office=i)
    # create employees
    for i in Department.objects.all():
        for _ in range(employee_count):
            Employee.objects.create(name=fake.name(), salary=randint(5000, 50000), date_of_issue=fake.date(), department=i)
