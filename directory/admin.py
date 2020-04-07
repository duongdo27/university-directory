"""
Create admin view to manage the university directory
"""
# pylint: disable=unnecessary-pass

from django.contrib import admin

from directory.models import Department
from directory.models import Professor
from directory.models import Course
from directory.models import Student
from directory.models import Grade


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    """
    Admin view on department
    """


@admin.register(Professor)
class ProfessorAdmin(admin.ModelAdmin):
    """
    Admin view on professor
    """
    list_display = ("__str__", "phone", "email", "department")
    list_filter = ("department", )
    search_fields = ("first_name", "last_name", "phone", "email")


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    """
    Admin view on course
    """
    list_display = ("name", "professor")
    list_filter = ("professor__department", )
    search_fields = ("name", "professor__first_name", "professor__last_name")


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    """
    Admin view on student
    """
    list_display = ("__str__", "email", "year")
    list_filter = ("year", )
    search_fields = ("first_name", "last_name", "email")


@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    """
    Admin view on grade
    """
    list_display = ("student", "course", "grade")
    list_filter = ("grade", "course__professor__department")
    search_fields = ("student__first_name", "student__last_name", "course")
