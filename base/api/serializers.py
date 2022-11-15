from base.models import Department, Employee
from rest_framework import serializers


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = (
            'id',
            'name',
            'head_office',
        )
        read_only_fields = fields


class DepartmentPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = (
            'id',
            'name',
            'head_office',
        )
        extra_kwargs = {
            'name': {
                'required': False
            }
        }


class EmployeeSerializer(serializers.ModelSerializer):
    department = serializers.StringRelatedField()

    class Meta:
        model = Employee
        fields = (
            'id',
            'name',
            'salary',
            'date_of_issue',
            'department',
        )
        read_only_fields = fields


class EmployeePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = (
            'id',
            'name',
            'salary',
            'date_of_issue',
            'department',
        )
        extra_kwargs = {
            'name': {
                'required': False
            },
            'salary': {
                'required': False
            },
            'date_of_issue': {
                'required': False
            },
            'department': {
                'required': False
            }
        }
