from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework import pagination
from rest_framework.response import Response

from .serializers import DepartmentSerializer, DepartmentPostSerializer, EmployeeSerializer, EmployeePostSerializer
from ..models import Department, Employee


class CustomPagination(pagination.PageNumberPagination):
    def get_paginated_response(self, data):
        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'count': self.page.paginator.count,
            'results': data,
            'page_size': self.page_size,
        })

@api_view(['GET', 'POST'])
def department_list(request):
    if request.method == 'GET':
        departments = Department.objects.all()
        serializer = DepartmentSerializer(departments, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = DepartmentPostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


@api_view(['GET'])
def department_list_by_parent_department(request, department_id=None):
    if request.method == 'GET':
        departments = Department.objects.filter(head_office=department_id)
        serializer = DepartmentSerializer(departments, many=True)
        return Response(serializer.data)


@api_view(['GET', 'PUT', 'POST', 'DELETE'])
def department_detail(request, department_id=None):
    try:
        department = Department.objects.get(pk=department_id)
    except Department.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = DepartmentSerializer(department)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = DepartmentPostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(head_office=department)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PUT':
        serializer = DepartmentPostSerializer(department, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        department.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def employee_list(request, department_id=None):
    try:
        department = Department.objects.get(id=department_id)
    except Department.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        paginator = CustomPagination()
        employees = Employee.objects.filter(department=department)
        result_page = paginator.paginate_queryset(employees, request)
        serializer = EmployeeSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    elif request.method == 'POST':
        serializer = EmployeePostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(department_id=department_id)
            return Response(serializer.data)
        return Response(serializer.errors)


@api_view(['GET', 'PUT', 'DELETE'])
def employee_detail(request, employee_id=None):
    try:
        employee = Employee.objects.get(pk=employee_id)
    except Employee.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = EmployeePostSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
