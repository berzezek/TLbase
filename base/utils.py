def create_tl_base(department_depth_level = 5, department_count_for_each_head_office = 2, employee_count = 5):
    from .models import Department, Employee
    from faker import Faker
    fake = Faker([ 'ru_RU' ])
    # create departments and subdivisions
    Department.objects.create(name=fake.bs(), head_office=None)
    dep = Department.objects.all()
    dep.save()
    base_count = dep.count()
    for _ in range(department_depth_level):
        for i in dep:
            for _ in range(department_count_for_each_head_office):
                d = Department.objects.create(name=fake.bs(), head_office=i)
                d.save()
                dep = Department.objects.filter(head_office__isnull=False)
                dep = dep[ base_count:base_count*department_count_for_each_head_office ]
        base_count *= department_count_for_each_head_office
    # create employees
    for i in Department.objects.all():
        for _ in range(employee_count):
            emp = Employee.objects.create(name=fake.name(), salary=fake.pyint() * 10, date_of_issue=fake.date(), department=i)
            emp.save()
