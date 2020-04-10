"""
Test all models
"""
# pylint: disable=no-member

from django.test import TestCase

from directory.models import Student
from directory.models import Grade
from directory.models import Department
from directory.models import Professor
from directory.models import Course


class BaseTest(TestCase):
    """
    Base test to set up all models
    """

    def setUp(self):
        self.department = Department.objects.create(name="History")
        self.professor = Professor.objects.create(
            first_name="John",
            last_name="Doe",
            email="jdoe@yahoo.com",
            phone="012345678",
            department=self.department)
        self.course = Course.objects.create(
            name="HIS111",
            description="Intro to history",
            professor=self.professor)
        self.student = Student.objects.create(
            first_name="Alan",
            last_name="Smith",
            email="as@yahoo.com",
            year="Sophomore")
        self.grade = Grade.objects.create(
            grade="A", course=self.course, student=self.student)


class DepartmentTest(BaseTest):
    """
    Test department model
    """

    def test_string_representation(self):
        """
        Test department name
        """
        self.assertEqual(str(self.department), self.department.name)


class ProfessorTest(BaseTest):
    """
    Test professor model
    """

    def test_string_representation(self):
        """
        Test professor name
        """
        self.assertEqual(str(self.professor), "Doe, John")


class CourseTest(BaseTest):
    """
    Test course model
    """

    def test_string_representation(self):
        """
        Test course name
        """
        self.assertEqual(str(self.course), self.course.name)


class StudentTest(BaseTest):
    """
    Test student model
    """

    def test_string_representation(self):
        """
        Test student name
        """
        self.assertEqual(str(self.student), "Smith, Alan")


class GradeTest(BaseTest):
    """
    Test grade model
    """

    def test_string_representation(self):
        """
        Test grade value
        """
        self.assertEqual(str(self.grade), "A")
