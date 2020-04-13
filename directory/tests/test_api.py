"""
Test all APIs
"""
# pylint: disable=too-many-instance-attributes
# pylint: disable=no-member

from rest_framework.test import APITestCase

from directory.models import Student
from directory.models import Grade
from directory.models import Professor
from directory.models import Course
from directory.models import Department


class BaseTest(APITestCase):
    """
    Base test to set up all models
    """
    def setUp(self):
        """
        Set up all models
        """
        self.department2 = Department.objects.create(name="Computer")
        self.department1 = Department.objects.create(name="History")
        self.professor2 = Professor.objects.create(first_name="Jane",
                                                   last_name="Do",
                                                   email="jdo@yahoo.com",
                                                   phone="0123456789",
                                                   department=self.department1)
        self.professor1 = Professor.objects.create(first_name="John",
                                                   last_name="Doe",
                                                   email="jdoe@yahoo.com",
                                                   phone="012345678",
                                                   department=self.department1)
        self.course1 = Course.objects.create(name="HIS111",
                                             description="Intro to History",
                                             professor=self.professor1)
        self.course2 = Course.objects.create(name="CS111",
                                             description="Intro to CS",
                                             professor=self.professor2)
        self.student1 = Student.objects.create(first_name="Alan",
                                               last_name="Smith",
                                               email="as@yahoo.com",
                                               year="Sophomore")
        self.student2 = Student.objects.create(first_name="Harry",
                                               last_name="Pogba",
                                               email="hp@yahoo.com",
                                               year="Junior")
        self.grade = Grade.objects.create(grade="A",
                                          course=self.course1,
                                          student=self.student1)


class CourseListAPIViewTest(BaseTest):
    """
    Test course list view
    """
    def test(self):
        """
        Test if course data return correctly
        """
        response = self.client.get('/api/course_list')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, [{
            'description': 'Intro to History',
            'gpa': 4.0,
            'name': 'HIS111',
            'professor': 'Doe, John'
        }, {
            'description': 'Intro to CS',
            'gpa': None,
            'name': 'CS111',
            'professor': 'Do, Jane'
        }])


class CourseGradesAPIViewTest(BaseTest):
    """
    Test course grade view
    """
    def test_no_name(self):
        """
        Test no parameter given
        """
        response = self.client.get('/api/course_grades')
        self.assertEqual(response.status_code, 400)

    def test_not_found(self):
        """
        Test wrong parameter
        """
        response = self.client.get('/api/course_grades?name=fjerioj')
        self.assertEqual(response.status_code, 404)

    def test_found(self):
        """
        Test if course data return correctly
        """
        response = self.client.get('/api/course_grades?name=HIS111')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, [
            {
                'student': 'Smith, Alan',
                'grade': 'A',
            },
        ])


class StudentListAPIViewTest(BaseTest):
    """
    Test student list view
    """
    def test(self):
        """
        Test if student data return correctly
        """
        response = self.client.get('/api/student_list')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, [{
            'name': "Smith, Alan",
            'email': "as@yahoo.com",
            'year': "Sophomore",
            'gpa': 4.0,
        }, {
            'name': "Pogba, Harry",
            'email': "hp@yahoo.com",
            'year': "Junior",
            'gpa': None,
        }])


class StudentGradesAPIViewTest(BaseTest):
    """
    Test student grade view
    """
    def test_no_name(self):
        """
        Test no parameter given
        """
        response = self.client.get('/api/student_grades')
        self.assertEqual(response.status_code, 400)

    def test_not_found(self):
        """
        Test wrong parameter
        """
        response = self.client.get(
            '/api/student_grades?first_name=fjerioj&last_name=reers')
        self.assertEqual(response.status_code, 404)

    def test_found(self):
        """
        Test if course data return correctly
        """
        response = self.client.get(
            '/api/student_grades?first_name=Alan&last_name=Smith')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, [
            {
                'course': "HIS111",
                'grade': "A",
            },
        ])


class UpdateGradeAPIViewTest(BaseTest):
    """
    Test update grade view
    """
    def test_no_grade(self):
        """
        Test no grade given
        """
        data = {"first_name": "Alan", "last_name": "Smith", "course": "HIS111"}
        response = self.client.post('/api/update_grade',
                                    data=data,
                                    format='json')
        self.assertEqual(response.status_code, 400)

    def test_no_student(self):
        """
        Test no student given
        """
        data = {"grade": "C", "course": "HIS111"}
        response = self.client.post('/api/update_grade',
                                    data=data,
                                    format='json')
        self.assertEqual(response.status_code, 400)

    def test_no_course(self):
        """
        Test no course given
        """
        data = {"first_name": "Alan", "last_name": "Smith", "grade": "C"}
        response = self.client.post('/api/update_grade',
                                    data=data,
                                    format='json')
        self.assertEqual(response.status_code, 400)

    def test_not_found_student(self):
        """
        Test not found student
        """
        data = {
            "grade": "C",
            "first_name": "Hello",
            "last_name": "Smith",
            "course": "HIS111"
        }
        response = self.client.post('/api/update_grade',
                                    data=data,
                                    format='json')
        self.assertEqual(response.status_code, 404)

    def test_not_found_course(self):
        """
        Test not found course
        """
        data = {
            "grade": "C",
            "first_name": "Alan",
            "last_name": "Smith",
            "course": "HIS114"
        }
        response = self.client.post('/api/update_grade',
                                    data=data,
                                    format='json')
        self.assertEqual(response.status_code, 404)

    def test_update_existing_grade(self):
        """
        Test updating existing grade
        """
        data = {
            "grade": "C",
            "first_name": "Alan",
            "last_name": "Smith",
            "course": "HIS111"
        }
        response = self.client.post('/api/update_grade',
                                    data=data,
                                    format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, {"message": "OK"})
        self.grade.refresh_from_db()
        self.assertEqual(self.grade.grade, 'C')

    def test_create_new_grade(self):
        """
        Test create new grade
        """
        data = {
            "grade": "C",
            "first_name": "Harry",
            "last_name": "Pogba",
            "course": "HIS111"
        }
        response = self.client.post('/api/update_grade',
                                    data=data,
                                    format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, {"message": "OK"})
        new_grade = Grade.objects.filter(student=self.student2,
                                         course=self.course1,
                                         grade='C').first()
        self.assertIsNotNone(new_grade)
