from django.contrib import admin
from django.utils.html import format_html, urlencode
from django.urls import reverse
from .models import Category, Employee


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    def parent_category(self, obj):
        parent_category = []
        category = obj.category
        while category is not None:
            parent_category.append(category)
            category = category.category
        return f'{" -> ".join([c.name for c in parent_category[::-1]])}'

    list_display = (
        'name',
        'parent_category',
        'add_subcategory',
        'edit_category',
        'view_employee',
        'add_employee',
        'remove_category',
    )
    ordering = ('id',)

    def view_employee(self, obj):
        count = obj.employee_set.count()
        url = (
            f'/admin/base/employee/?category__id__exact={obj.id}'
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

    def add_subcategory(self, obj):
        url = (
                reverse('admin:base_category_add') + "?" +
                urlencode({'category': obj.id})
        )
        return format_html(f'<a href="{url}">Добавить подотдел</a>')

    def add_employee(self, obj):
        url = (
                reverse('admin:base_employee_add') + "?" +
                urlencode({'category': obj.id})
        )
        return format_html(f'<a href="{url}">Добавить сотрудника</a>')

    def edit_category(self, obj):
        url = (
            reverse('admin:base_category_change', args=[ obj.id ])
        )
        return format_html(f'<a href="{url}" style="color: green">Изменить отдел</a>')

    def remove_category(self, obj):
        url = (
            reverse('admin:base_category_delete', args=[ obj.id ])
        )
        return format_html(f'<a href="{url}" style="color: red">Remove Category</a>')

    view_employee.short_description = 'Сотрудники'
    add_employee.short_description = 'Добавить сотрудника'
    add_subcategory.short_description = 'Добавить подкатегорию'
    edit_category.short_description = 'Изменить категорию'
    remove_category.short_description = 'Удалить категорию'
    parent_category.short_description = 'Головной отдел'

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields[ "name" ].label = "Наименование отдела:"
        form.base_fields[ "category" ].label = "Головной отдел:"
        return form

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'salary',
        'date_of_issue',
        'category',
        'add_employee',
        'edit_employee',
        'remove_employee',
    )
    def add_employee(self, obj):
        url = (
                reverse('admin:base_employee_add') + "?" +
                urlencode({'category': obj.id})
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

    list_filter = ('category',)
    search_fields = ('name__startswith', 'category__name__startswith')
    # raw_id_fields = ('category',)
    ordering = []

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields[ "name" ].label = "Ф.И.О.:"
        form.base_fields[ "salary" ].label = "Заработная плата:"
        form.base_fields[ "date_of_issue" ].label = "Дата приказа:"
        form.base_fields[ "category" ].label = "Головной отдел:"
        return form