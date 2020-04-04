from django.contrib import admin

from directory.models import Department
from directory.models import Professor
from directory.models import Course
from directory.models import Student


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    pass


@admin.register(Professor)
class ProfessorAdmin(admin.ModelAdmin):
    list_display = ("__str__", "phone", "email", "department")


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    pass

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("__str__", "email", "year")