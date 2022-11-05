from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=100, verbose_name='Отдел')
    head_office = models.ForeignKey('Department', on_delete=models.CASCADE, null=True,
                                    blank=True, verbose_name='Головной отдел')

    class Meta:
        verbose_name = 'Отдел'
        verbose_name_plural = 'Отделы'
        ordering = ('id',)

    def __str__(self):
        return self.name


class Employee(models.Model):
    name = models.CharField(max_length=50, verbose_name='ФИО')
    salary = models.IntegerField(verbose_name='Зарплата')
    date_of_issue = models.DateField(verbose_name='Дата принятия на работу')
    department = models.ForeignKey(Department, on_delete=models.CASCADE, verbose_name='Отдел')

    class Meta:
        verbose_name = 'Сотрудника'
        verbose_name_plural = 'Сотрудники'
        ordering = ('id',)

    def __str__(self):
        return self.name
