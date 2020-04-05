"""
URLs for University app
"""
#pylint: disable=invalid-name
from django.urls import path

from directory import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('department_list', views.DepartmentListView.as_view(), name='department_list'),
    path('department/<int:pk>', views.DepartmentDetailView.as_view(), name='department_detail'),
    path('department_update/<int:pk>', views.DepartmentUpdateView.as_view(), name='department_update'),
    path('department_create', views.DepartmentCreateView.as_view(), name='department_create'),
    path('department_delete/<int:pk>', views.DepartmentDeleteView.as_view(), name='department_delete'),
    path('professor_list', views.ProfessorListView.as_view(), name='professor_list'),
    path('professor/<int:pk>', views.ProfessorDetailView.as_view(), name='professor_detail'),
    path('professor_update/<int:pk>', views.ProfessorUpdateView.as_view(), name='professor_update'),
    path('professor_create', views.ProfessorCreateView.as_view(), name='professor_create'),
    path('professor_delete/<int:pk>', views.ProfessorDeleteView.as_view(), name='professor_delete'),
    path('course_list', views.CourseListView.as_view(), name='course_list'),
    path('course/<int:pk>', views.CourseDetailView.as_view(), name='course_detail'),
    path('course_update/<int:pk>', views.CourseUpdateView.as_view(), name='course_update'),
    path('course_create', views.CourseCreateView.as_view(), name='course_create'),
    path('course_delete/<int:pk>', views.CourseDeleteView.as_view(), name='course_delete'),
    path('student_list', views.StudentListView.as_view(), name='student_list'),
    path('student/<int:pk>', views.StudentDetailView.as_view(), name='student_detail'),
    path('student_update/<int:pk>', views.StudentUpdateView.as_view(), name='student_update'),
    path('student_create', views.StudentCreateView.as_view(), name='student_create'),
    path('student_delete/<int:pk>', views.StudentDeleteView.as_view(), name='student_delete'),
    path('grade_update/<int:pk>', views.GradeUpdateView.as_view(), name='grade_update'),
    path('grade_create', views.GradeCreateView.as_view(), name='grade_create'),
    path('grade_delete/<int:pk>', views.GradeDeleteView.as_view(), name='grade_delete'),
]