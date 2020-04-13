"""
API View for the directory app
"""

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import ParseError
from django.shortcuts import get_object_or_404
from directory.models import Course
from directory.models import Student


class CourseListAPIView(APIView):
    def get(self, request):
        courses = Course.objects.all()
        data = [{
            'name': course.name,
            'professor': str(course.professor),
            'description': course.description,
            'gpa': course.gpa,
        } for course in courses]
        return Response(data)


class CourseGradesAPIView(APIView):
    def get(self, request):
        name = request.query_params.get('name')
        if not name:
            raise ParseError('No name provided')

        course = get_object_or_404(Course, name=name)
        grades = course.grades
        data = [{
            'student': str(grade.student),
            'grade': grade.grade,
        } for grade in grades]
        return Response(data)


class StudentListAPIView(APIView):
    def get(self, request):
        students = Student.objects.all()
        data = [{
            'name': str(student),
            'email': student.email,
            'year': student.year,
            'gpa': student.gpa,
        } for student in students]
        return Response(data)


class StudentGradesAPIView(APIView):
    def get(self, request):
        first_name = request.query_params.get('first_name')
        last_name = request.query_params.get('last_name')

        if not first_name or not last_name:
            raise ParseError('No first_name  or last_name provided')

        student = get_object_or_404(Student,
                                    first_name=first_name,
                                    last_name=last_name)
        grades = student.grades
        data = [{
            'course': str(grade.course),
            'grade': grade.grade,
        } for grade in grades]
        return Response(data)
