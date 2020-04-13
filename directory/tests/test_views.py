"""
Test all views
"""
# pylint: disable=no-member
# pylint: disable=dangerous-default-value
# pylint: disable=too-many-instance-attributes

from django.test import TestCase
from django.test import RequestFactory
from django.template.response import TemplateResponse
from django.urls import reverse_lazy

from directory.models import Professor
from directory.models import Course
from directory.models import Department
from directory.models import Student
from directory.models import Grade
from directory.views import IndexView
from directory.views import DepartmentCreateView
from directory.views import DepartmentDetailView
from directory.views import DepartmentDeleteView
from directory.views import DepartmentListView
from directory.views import DepartmentUpdateView
from directory.views import ProfessorCreateView
from directory.views import ProfessorDeleteView
from directory.views import ProfessorListView
from directory.views import ProfessorDetailView
from directory.views import ProfessorUpdateView
from directory.views import CourseListView
from directory.views import CourseDetailView
from directory.views import CourseCreateView
from directory.views import CourseUpdateView
from directory.views import CourseDeleteView
from directory.views import StudentListView
from directory.views import StudentDetailView
from directory.views import StudentCreateView
from directory.views import StudentUpdateView
from directory.views import StudentDeleteView
from directory.views import GradeCreateView
from directory.views import GradeDeleteView
from directory.views import GradeUpdateView


def _get_response(view_class, request, kwargs={}):
    """
    :param view_class: the view class to test
    :param request: the request
    :param kwargs: list of key words
    :return: the response
    """
    response = view_class.as_view()(request, **kwargs)
    if isinstance(response, TemplateResponse):
        response.render()
    return response


class BaseTest(TestCase):
    """
    Base test to set up all models
    """
    def setUp(self):
        """
        Set up all models
        """
        self.factory = RequestFactory()

        self.department1 = Department.objects.create(name="History")
        self.department2 = Department.objects.create(name="Computer")
        self.professor1 = Professor.objects.create(first_name="John",
                                                   last_name="Doe",
                                                   email="jdoe@yahoo.com",
                                                   phone="012345678",
                                                   department=self.department1)
        self.professor2 = Professor.objects.create(first_name="Jane",
                                                   last_name="Do",
                                                   email="jdo@yahoo.com",
                                                   phone="0123456789",
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


class IndexViewTest(BaseTest):
    """
    Test the application home page view
    """
    def test(self):
        """
        Test if home page render correctly
        """
        request = self.factory.get('')
        response = _get_response(IndexView, request)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Welcome to university directory!", response.content)


class DepartmentListViewTest(BaseTest):
    """
    Test the department home page view
    """
    def test(self):
        """
        Test if department home page render correctly
        """
        request = self.factory.get('')
        response = _get_response(DepartmentListView, request)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Departments", response.content)
        self.assertIn(b"History", response.content)
        self.assertEqual(list(response.context_data['departments']),
                         [self.department2, self.department1])


class DepartmentDetailViewTest(BaseTest):
    """
    Test the department detail page view
    """
    def test(self):
        """
        Test if department detail page render correctly
        """
        request = self.factory.get('')
        response = _get_response(DepartmentDetailView,
                                 request,
                                 kwargs={"pk": self.department1.id})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Department History", response.content)
        self.assertIn(b"Doe, John", response.content)
        self.assertIn(b"jdoe@yahoo.com", response.content)
        self.assertIn(b"012345678", response.content)
        self.assertEqual(response.context_data['department'], self.department1)


class DepartmentCreateViewTest(BaseTest):
    """
    Test the department create page view
    """
    def test_get(self):
        """
        Test if department create page render correctly
        """
        request = self.factory.get('')
        response = _get_response(DepartmentCreateView, request)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Create Department", response.content)
        self.assertIn(b"Name", response.content)
        self.assertIn(b"Create", response.content)
        self.assertIn(b"Cancel", response.content)

    def test_post(self):
        """
        Test if information to create new department post successfully
        """
        request = self.factory.post('', data={'name': 'Biology'})
        response = _get_response(DepartmentCreateView, request)
        self.assertEqual(response.status_code, 302)

        new_department = Department.objects.filter(name='Biology').first()
        self.assertIsNotNone(new_department)
        self.assertEqual(
            response.url,
            reverse_lazy('department_detail', kwargs={'pk':
                                                      new_department.id}))


class DepartmentUpdateViewTest(BaseTest):
    """
    Test the department update page view
    """
    def test_get(self):
        """
        Test if department update page render correctly
        """
        request = self.factory.get('')
        response = _get_response(DepartmentUpdateView,
                                 request,
                                 kwargs={'pk': self.department2.id})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Update Department", response.content)
        self.assertIn(b"Name", response.content)
        self.assertIn(b"Save", response.content)
        self.assertIn(b"Cancel", response.content)

    def test_post(self):
        """
        Test if information to update department post successfully
        """
        request = self.factory.post('', data={'name': 'World'})
        response = _get_response(DepartmentUpdateView,
                                 request,
                                 kwargs={'pk': self.department2.id})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(
            response.url,
            reverse_lazy('department_detail',
                         kwargs={'pk': self.department2.id}))
        self.department2.refresh_from_db()
        self.assertEqual(self.department2.name, 'World')


class DepartmentDeleteViewTest(BaseTest):
    """
    Test the department delete page view
    """
    def test_get(self):
        """
        Test if department delete page render correctly
        """
        request = self.factory.get('')
        response = _get_response(DepartmentDeleteView,
                                 request,
                                 kwargs={'pk': self.department2.id})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Delete Department", response.content)
        self.assertIn(b"Are you sure you want to delete", response.content)
        self.assertIn(b"Confirm", response.content)
        self.assertIn(b"Cancel", response.content)

    def test_post(self):
        """
        Test if information to delete department post successfully
        """
        request = self.factory.post('')
        response = _get_response(DepartmentDeleteView,
                                 request,
                                 kwargs={'pk': self.department2.id})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse_lazy('department_list'))
        self.assertEqual(len(Department.objects.filter(name='Computer')), 0)


class ProfessorListViewTest(BaseTest):
    """
    Test the professor home page view
    """
    def test(self):
        """
        Test if professor home page render correctly
        """
        request = self.factory.get('')
        response = _get_response(ProfessorListView, request)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Doe, John", response.content)
        self.assertIn(b"Do, Jane", response.content)
        self.assertEqual(list(response.context_data['professors']),
                         [self.professor2, self.professor1])


class ProfessorDetailViewTest(BaseTest):
    """
    Test the professor detail page view
    """
    def test(self):
        """
        Test if professor detail page render correctly
        """
        request = self.factory.get('')
        response = _get_response(ProfessorDetailView,
                                 request,
                                 kwargs={"pk": self.professor1.id})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Doe, John", response.content)
        self.assertIn(b"HIS111", response.content)
        self.assertIn(b"Intro to History", response.content)
        self.assertEqual(response.context_data['professor'], self.professor1)


class ProfessorCreateViewTest(BaseTest):
    """
    Test the professor create page view
    """
    def test_get(self):
        """
        Test if professor create page render correctly
        """
        request = self.factory.get('')
        response = _get_response(ProfessorCreateView, request)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Create Professor", response.content)
        self.assertIn(b"First name", response.content)
        self.assertIn(b"Last name", response.content)
        self.assertIn(b"Email", response.content)
        self.assertIn(b"Phone", response.content)
        self.assertIn(b"Department", response.content)
        self.assertIn(b"Create", response.content)
        self.assertIn(b"Cancel", response.content)

    def test_post(self):
        """
        Test if information to create professor post successfully
        """
        request = self.factory.post('',
                                    data={
                                        'first_name': 'Alex',
                                        'last_name': 'Smith',
                                        'email': 'as@yahoo.com',
                                        'phone': '47298374',
                                        'department': self.department1.id
                                    })
        response = _get_response(ProfessorCreateView, request)
        self.assertEqual(response.status_code, 302)

        new_professor = Professor.objects.filter(email='as@yahoo.com').first()
        self.assertIsNotNone(new_professor)
        self.assertEqual(
            response.url,
            reverse_lazy('professor_detail', kwargs={'pk': new_professor.id}))


class ProfessorUpdateViewTest(BaseTest):
    """
    Test the professor update page view
    """
    def test_get(self):
        """
        Test if professor update page render correctly
        """
        request = self.factory.get('')
        response = _get_response(ProfessorUpdateView,
                                 request,
                                 kwargs={'pk': self.professor2.id})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Update Professor", response.content)
        self.assertIn(b"First name", response.content)
        self.assertIn(b"Last name", response.content)
        self.assertIn(b"Email", response.content)
        self.assertIn(b"Phone", response.content)
        self.assertIn(b"Department", response.content)
        self.assertIn(b"Save", response.content)
        self.assertIn(b"Cancel", response.content)

    def test_post(self):
        """
        Test if information to update professor post successfully
        """
        request = self.factory.post('',
                                    data={
                                        'first_name': 'Janey',
                                        'last_name': 'Do',
                                        'email': 'jdo@yahoo.com',
                                        'phone': '0123456789',
                                        'department': self.department1.id
                                    })
        response = _get_response(ProfessorUpdateView,
                                 request,
                                 kwargs={'pk': self.professor2.id})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(
            response.url,
            reverse_lazy('professor_detail', kwargs={'pk':
                                                     self.professor2.id}))
        self.professor2.refresh_from_db()
        self.assertEqual(self.professor2.first_name, 'Janey')


class ProfessorDeleteViewTest(BaseTest):
    """
    Test the professor delete page view
    """
    def test_get(self):
        """
        Test if professor delete page render correctly
        """
        request = self.factory.get('')
        response = _get_response(ProfessorDeleteView,
                                 request,
                                 kwargs={'pk': self.professor2.id})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Delete Professor", response.content)
        self.assertIn(b"Are you sure you want to delete", response.content)
        self.assertIn(b"Confirm", response.content)
        self.assertIn(b"Cancel", response.content)

    def test_post(self):
        """
        Test if information to delete professor post successfully
        """
        request = self.factory.post('')
        response = _get_response(ProfessorDeleteView,
                                 request,
                                 kwargs={'pk': self.professor2.id})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse_lazy('professor_list'))
        self.assertEqual(len(Professor.objects.filter(email='jdo@yahoo.com')),
                         0)


class CourseListViewTest(BaseTest):
    """
    Test the course home page view
    """
    def test(self):
        """
        Test if course home page render correctly
        """
        request = self.factory.get('')
        response = _get_response(CourseListView, request)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Course", response.content)
        self.assertIn(b"HIS111", response.content)
        self.assertIn(b"CS111", response.content)
        self.assertEqual(list(response.context_data['courses']),
                         [self.course2, self.course1])


class CourseDetailViewTest(BaseTest):
    """
    Test the course detail page view
    """
    def test(self):
        """
        Test if course detail page render correctly
        """
        request = self.factory.get('')
        response = _get_response(CourseDetailView,
                                 request,
                                 kwargs={"pk": self.course1.id})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Smith, Alan", response.content)
        self.assertIn(b"as@yahoo.com", response.content)
        self.assertIn(b"Sophomore", response.content)
        self.assertEqual(response.context_data['course'], self.course1)


class CourseCreateViewTest(BaseTest):
    """
    Test the course create page view
    """
    def test_get(self):
        """
        Test if course create page render correctly
        """
        request = self.factory.get('')
        response = _get_response(CourseCreateView, request)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Create Course", response.content)
        self.assertIn(b"Name", response.content)
        self.assertIn(b"Description", response.content)
        self.assertIn(b"Professor", response.content)
        self.assertIn(b"Create", response.content)
        self.assertIn(b"Cancel", response.content)

    def test_post(self):
        """
        Test if information to create course post successfully
        """
        request = self.factory.post('',
                                    data={
                                        'name': 'CS200',
                                        'description': 'Data Structure',
                                        'professor': self.professor2.id
                                    })
        response = _get_response(CourseCreateView, request)
        self.assertEqual(response.status_code, 302)

        new_course = Course.objects.filter(name='CS200').first()
        self.assertIsNotNone(new_course)
        self.assertEqual(
            response.url,
            reverse_lazy('course_detail', kwargs={'pk': new_course.id}))


class CourseUpdateViewTest(BaseTest):
    """
    Test the course update page view
    """
    def test_get(self):
        """
        Test if course update page render correctly
        """
        request = self.factory.get('')
        response = _get_response(CourseUpdateView,
                                 request,
                                 kwargs={'pk': self.course1.id})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Edit Course", response.content)
        self.assertIn(b"Name", response.content)
        self.assertIn(b"Description", response.content)
        self.assertIn(b"Professor", response.content)
        self.assertIn(b"Save", response.content)
        self.assertIn(b"Cancel", response.content)

    def test_post(self):
        """
        Test if information to update course post successfully
        """
        request = self.factory.post('',
                                    data={
                                        'name': 'HIS111',
                                        'description': 'World history',
                                        'professor': self.professor1.id
                                    })
        response = _get_response(CourseUpdateView,
                                 request,
                                 kwargs={'pk': self.course1.id})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(
            response.url,
            reverse_lazy('course_detail', kwargs={'pk': self.course1.id}))
        self.course1.refresh_from_db()
        self.assertEqual(self.course1.description, 'World history')


class CourseDeleteViewTest(BaseTest):
    """
    Test the course delete page view
    """
    def test_get(self):
        """
        Test if course delete page render correctly
        """
        request = self.factory.get('')
        response = _get_response(CourseDeleteView,
                                 request,
                                 kwargs={'pk': self.course1.id})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Delete Course", response.content)
        self.assertIn(b"Are you sure you want to delete", response.content)
        self.assertIn(b"Confirm", response.content)
        self.assertIn(b"Cancel", response.content)

    def test_post(self):
        """
        Test if information to delete course post successfully
        """
        request = self.factory.post('')
        response = _get_response(CourseDeleteView,
                                 request,
                                 kwargs={'pk': self.course1.id})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse_lazy('course_list'))
        self.assertEqual(len(Course.objects.filter(name='HIS111')), 0)


class StudentListViewTest(BaseTest):
    """
    Test the student home page view
    """
    def test(self):
        """
        Test if student home page render correctly
        """
        request = self.factory.get('')
        response = _get_response(StudentListView, request)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Students", response.content)
        self.assertIn(b"Pogba, Harry", response.content)
        self.assertIn(b"Smith, Alan", response.content)
        self.assertEqual(list(response.context_data['students']),
                         [self.student2, self.student1])


class StudentDetailViewTest(BaseTest):
    """
    Test the student detail page view
    """
    def test(self):
        """
        Test if student detail page render correctly
        """
        request = self.factory.get('')
        response = _get_response(StudentDetailView,
                                 request,
                                 kwargs={"pk": self.student1.id})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Student Smith, Alan", response.content)
        self.assertIn(b"as@yahoo.com", response.content)
        self.assertIn(b"Sophomore", response.content)
        self.assertIn(b"HIS111", response.content)
        self.assertEqual(response.context_data['student'], self.student1)


class StudentCreateViewTest(BaseTest):
    """
    Test the student create page view
    """
    def test_get(self):
        """
        Test if student create page render correctly
        """
        request = self.factory.get('')
        response = _get_response(StudentCreateView, request)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Create Student", response.content)
        self.assertIn(b"First name", response.content)
        self.assertIn(b"Last name", response.content)
        self.assertIn(b"Email", response.content)
        self.assertIn(b"Year", response.content)
        self.assertIn(b"Create", response.content)
        self.assertIn(b"Cancel", response.content)

    def test_post(self):
        """
        Test if information to create student post successfully
        """
        request = self.factory.post('',
                                    data={
                                        'first_name': 'John',
                                        'last_name': 'Martial',
                                        'email': 'jm@yahoo.com',
                                        'phone': '8345903248',
                                        'year': 'Senior'
                                    })
        response = _get_response(StudentCreateView, request)
        self.assertEqual(response.status_code, 302)
        new_student = Student.objects.filter(email='jm@yahoo.com').first()
        self.assertIsNotNone(new_student)
        self.assertEqual(
            response.url,
            reverse_lazy('student_detail', kwargs={'pk': new_student.id}))


class StudentUpdateViewTest(BaseTest):
    """
    Test the student update page view
    """
    def test_get(self):
        """
        Test if student update page render correctly
        """
        request = self.factory.get('')
        response = _get_response(StudentUpdateView,
                                 request,
                                 kwargs={'pk': self.student1.id})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Update Student", response.content)
        self.assertIn(b"First name", response.content)
        self.assertIn(b"Last name", response.content)
        self.assertIn(b"Email", response.content)
        self.assertIn(b"Year", response.content)
        self.assertIn(b"Save", response.content)
        self.assertIn(b"Cancel", response.content)

    def test_post(self):
        """
        Test if information to update student post successfully
        """
        request = self.factory.post('',
                                    data={
                                        'first_name': 'Tony',
                                        'last_name': 'Smith',
                                        'email': 'as@yahoo.com',
                                        'year': self.student1.year
                                    })
        response = _get_response(StudentUpdateView,
                                 request,
                                 kwargs={'pk': self.student1.id})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(
            response.url,
            reverse_lazy('student_detail', kwargs={'pk': self.student1.id}))
        self.student1.refresh_from_db()
        self.assertEqual(self.student1.first_name, 'Tony')


class StudentDeleteViewTest(BaseTest):
    """
    Test the student delete page view
    """
    def test_get(self):
        """
        Test if student delete page render correctly
        """
        request = self.factory.get('')
        response = _get_response(StudentDeleteView,
                                 request,
                                 kwargs={'pk': self.student1.id})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Delete Student", response.content)
        self.assertIn(b"Are you sure you want to delete", response.content)
        self.assertIn(b"Confirm", response.content)
        self.assertIn(b"Cancel", response.content)

    def test_post(self):
        """
        Test if information to delete student post successfully
        """
        request = self.factory.post('')
        response = _get_response(StudentDeleteView,
                                 request,
                                 kwargs={'pk': self.student1.id})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse_lazy('student_list'))
        self.assertEqual(len(Student.objects.filter(email='as@yahoo.com')), 0)


class GradeCreateViewTest(BaseTest):
    """
    Test the grade create page view
    """
    def test_get(self):
        """
        Test if grade create page render correctly
        """
        request = self.factory.get('')
        response = _get_response(GradeCreateView,
                                 request,
                                 kwargs={'student_id': self.student1.id})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Smith, Alan", response.content)
        self.assertIn(b"Grade", response.content)
        self.assertIn(b"Course", response.content)
        self.assertIn(b"Create", response.content)
        self.assertIn(b"Cancel", response.content)

    def test_post(self):
        """
        Test if information to create grade post successfully
        """
        request = self.factory.post('',
                                    data={
                                        'grade': 'D',
                                        'course': self.course2.id,
                                        'student': self.student1.id
                                    })

        response = _get_response(GradeCreateView,
                                 request,
                                 kwargs={'student_id': self.student1.id})
        self.assertEqual(response.status_code, 302)

        new_grade = Grade.objects.filter(student=self.student1,
                                         course=self.course2).first()
        self.assertIsNotNone(new_grade)
        self.assertEqual(
            response.url,
            reverse_lazy('student_detail', kwargs={'pk': self.student1.id}))


class GradeUpdateViewTest(BaseTest):
    """
    Test the grade update page view
    """
    def test_get(self):
        """
        Test if grade update page render correctly
        """
        request = self.factory.get('')
        response = _get_response(GradeUpdateView,
                                 request,
                                 kwargs={'pk': self.grade.id})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Update Grade", response.content)
        self.assertIn(b"Grade", response.content)
        self.assertIn(b"Student", response.content)
        self.assertIn(b"Course", response.content)
        self.assertIn(b"Save", response.content)
        self.assertIn(b"Cancel", response.content)

    def test_post(self):
        """
        Test if information to update grade post successfully
        """
        request = self.factory.post('',
                                    data={
                                        'grade': 'B',
                                        'course': self.course1.id,
                                        'student': self.student1.id
                                    })
        response = _get_response(GradeUpdateView,
                                 request,
                                 kwargs={'pk': self.grade.id})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(
            response.url,
            reverse_lazy('student_detail', kwargs={'pk': self.student1.id}))
        self.grade.refresh_from_db()
        self.assertEqual(self.grade.grade, 'B')


class GradeDeleteViewTest(BaseTest):
    """
    Test the grade delete page view
    """
    def test_get(self):
        """
        Test if grade delete page render correctly
        """
        request = self.factory.get('')
        response = _get_response(GradeDeleteView,
                                 request,
                                 kwargs={'pk': self.grade.id})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Delete Grade", response.content)
        self.assertIn(b"Are you sure you want to delete", response.content)
        self.assertIn(b"Confirm", response.content)
        self.assertIn(b"Cancel", response.content)

    def test_post(self):
        """
        Test if information to delete grade post successfully
        """
        request = self.factory.post('')
        response = _get_response(GradeDeleteView,
                                 request,
                                 kwargs={'pk': self.grade.id})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(
            response.url,
            reverse_lazy('student_detail', kwargs={'pk': self.student1.id}))
        self.assertEqual(
            len(
                Grade.objects.filter(course=self.course1,
                                     student=self.student1)), 0)
