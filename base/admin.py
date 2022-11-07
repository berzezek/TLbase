from django.contrib import admin
from django.utils.html import format_html, urlencode
from django.urls import reverse
from .models import Department, Employee


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    def parent_department(self, obj):
        parent_department = []
        department = obj.head_office
        while department is not None:
            parent_department.append(department)
            department = department.head_office
        return f'{" -> ".join([c.name for c in parent_department[::-1]])}'

    list_display = (
        'name',
        'parent_department',
        'add_head_office',
        'edit_department',
        'view_employee',
        'add_employee',
        'remove_department',
    )
    ordering = ('id',)

    def view_employee(self, obj):
        count = obj.employee_set.count()
        url = (
            f'/admin/base/employee/?department__id__exact={obj.id}'
        )
        if count > 0:
            if count % 10 == 1:
                return format_html(f'<a href="{url}">{count} сотрудник</a>')
            elif count % 10 in (2, 3, 4) and count not in (12, 13, 14):
                return format_html(f'<a href="{url}">{count} сотрудника</a>')
            else:
                return format_html(f'<a href="{url}">{count} сотрудников</a>')
        else:
            return format_html(f'Нет сотрудников')

    def add_head_office(self, obj):
        url = (
                reverse('admin:base_department_add') + "?" +
                urlencode({'department': obj.id})
        )
        return format_html(f'<a href="{url}">Добавить подотдел</a>')

    def add_employee(self, obj):
        url = (
                reverse('admin:base_employee_add') + "?" +
                urlencode({'department': obj.id})
        )
        return format_html(f'<a href="{url}">Добавить сотрудника</a>')

    def edit_department(self, obj):
        url = (
            reverse('admin:base_department_change', args=[ obj.id ])
        )
        return format_html(f'<a href="{url}" style="color: green">Изменить отдел</a>')

    def remove_department(self, obj):
        url = (
            reverse('admin:base_department_delete', args=[ obj.id ])
        )
        return format_html(f'<a href="{url}" style="color: red">Remove department</a>')

    view_employee.short_description = 'Сотрудники'
    add_employee.short_description = 'Добавить сотрудника'
    add_head_office.short_description = 'Добавить подкатегорию'
    edit_department.short_description = 'Изменить категорию'
    remove_department.short_description = 'Удалить категорию'
    parent_department.short_description = 'Головной отдел'

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields[ "name" ].label = "Наименование отдела:"
        form.base_fields[ "head_office" ].label = "Головной отдел:"
        return form

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'salary',
        'date_of_issue',
        'department',
        'add_employee',
        'edit_employee',
        'remove_employee',
    )
    def add_employee(self, obj):
        url = (
                reverse('admin:base_employee_add') + "?" +
                urlencode({'department': obj.id})
        )
        return format_html(f'<a href="{url}">Добавить сотрудника</a>')

    def remove_employee(self, obj):
        url = (
            reverse('admin:base_employee_delete', args=[ obj.id ])
        )
        return format_html(f'<a href="{url}" style="color: red">Удалить сотрудника</a>')

    def edit_employee(self, obj):
        url = (
            reverse('admin:base_employee_change', args=[ obj.id ])
        )
        return format_html(f'<a href="{url} style="color: green">Изменить сотрудника</a>')

    add_employee.short_description = 'Добавить сотрудника'
    edit_employee.short_description = 'Изменить сотрудника'
    remove_employee.short_description = 'Удалить cотрудника'

    list_filter = ('department',)
    search_fields = ('name__startswith', 'department__name__startswith')
    # raw_id_fields = ('department',)
    ordering = []

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields[ "name" ].label = "Ф.И.О.:"
        form.base_fields[ "salary" ].label = "Заработная плата:"
        form.base_fields[ "date_of_issue" ].label = "Дата приказа:"
        form.base_fields[ "department" ].label = "Головной отдел:"
        return form