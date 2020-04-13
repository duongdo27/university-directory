"""
API View for the directory app
"""
# pylint: disable=no-member
# pylint: disable=unused-argument
# pylint: disable=no-self-use

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import ParseError
from django.shortcuts import get_object_or_404
from directory.models import Course
from directory.models import Student
from directory.models import Grade


class CourseListAPIView(APIView):
    """
    API to get all courses
    """
    def get(self, request):
        """
        :param request: request
        :return: response contains all courses
        """
        courses = Course.objects.all()
        data = [{
            'name': course.name,
            'professor': str(course.professor),
            'description': course.description,
            'gpa': course.gpa,
        } for course in courses]
        return Response(data)


class CourseGradesAPIView(APIView):
    """
    API to get all grades in a course
    """
    def get(self, request):
        """
        :param request: request
        :return: response contains all grades in a course
        """
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
    """
    API to get all student
    """
    def get(self, request):
        """
        :param request: request
        :return: response contains all students
        """
        students = Student.objects.all()
        data = [{
            'name': str(student),
            'email': student.email,
            'year': student.year,
            'gpa': student.gpa,
        } for student in students]
        return Response(data)


class StudentGradesAPIView(APIView):
    """
    API to get all grades of a student
    """
    def get(self, request):
        """
        :param request: request
        :return: response contains all grades of a student
        """
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


class UpdateGradeAPIView(APIView):
    """
    API to update grade for a student in a course
    """
    def post(self, request):
        """
        :param request: request
        :return: response to update grades
        """
        grade = request.data.get('grade')
        if not grade:
            raise ParseError('No grade provided')
        first_name = request.data.get('first_name')
        last_name = request.data.get('last_name')

        if not first_name or not last_name:
            raise ParseError('No first_name  or last_name provided')

        course_name = request.data.get('course')
        if not course_name:
            raise ParseError('No course provided')

        student = get_object_or_404(Student,
                                    first_name=first_name,
                                    last_name=last_name)
        course = get_object_or_404(Course, name=course_name)
        Grade.objects.update_or_create(
            student=student,
            course=course,
            defaults={'grade': grade},
        )
        return Response({'message': 'OK'})
