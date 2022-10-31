from ..models import Category, Employee
from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):
    subcategories = serializers.StringRelatedField(many=True)
    class Meta:
        model = Category
        fields = (
            'id',
            'name',
            'category',
            'subcategories',
            'is_has_subcategories'
        )
        read_only_fields = fields

class CategoryPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'id',
            'name',
            'category',
        )
        extra_kwargs = {
            'name': {
                'required': False
            }
        }



class EmployeeSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    class Meta:
        model = Employee
        fields = (
            'id',
            'name',
            'salary',
            'date_of_issue',
            'category',
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
            'category',
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
            'category': {
                'required': False
            }
        }