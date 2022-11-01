from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='Категория')
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='subcategories', null=True, blank=True, verbose_name='Родительская категория')

    class Meta:
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'
        ordering = ('id',)
    def __str__(self):
        return self.name


class Employee(models.Model):
    name = models.CharField(max_length=50)
    salary = models.IntegerField()
    date_of_issue = models.DateField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Сотрудника'
        verbose_name_plural = 'Сотрудники'
        ordering = ('id',)

    def __str__(self):
        return self.name
