from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='subcategories', null=True, blank=True)

    def is_has_subcategories(self):
        return self.category is None

    def __str__(self):
        return self.name


class Employee(models.Model):
    name = models.CharField(max_length=50)
    salary = models.IntegerField()
    date_of_issue = models.DateField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name