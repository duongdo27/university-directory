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
    list_filter = ("department",)
    search_fields = ("first_name", "last_name", "phone", "email")


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("name", "professor")
    list_filter = ("professor__department",)
    search_fields = ("name", "professor__first_name", "professor__last_name")


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("__str__", "email", "year")
    list_filter = ("year",)
    search_fields = ("first_name", "last_name", "email")
