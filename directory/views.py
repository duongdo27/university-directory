from django.views.generic import TemplateView
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import UpdateView
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404

from directory.models import Department
from directory.forms import DepartmentForm
from directory.models import Professor
from directory.forms import ProfessorForm
from directory.models import Course
from directory.forms import CourseForm
from directory.models import Student
from directory.forms import StudentForm
from directory.models import Grade
from directory.forms import GradeCreateForm
from directory.forms import GradeUpdateForm

class IndexView(TemplateView):
    template_name = "index.html"


class DepartmentListView(ListView):
    template_name = "department/index.html"
    context_object_name = 'departments'

    def get_queryset(self):
        return Department.objects.all().order_by('name')


class DepartmentDetailView(DetailView):
    template_name = "department/detail.html"
    context_object_name = 'department'
    model = Department


class DepartmentUpdateView(UpdateView):
    template_name = "department/update.html"
    model = Department
    form_class = DepartmentForm

    def get_success_url(self):
        return reverse_lazy('department_detail', kwargs={'pk': self.object.id})


class DepartmentCreateView(CreateView):
    template_name = "department/create.html"
    model = Department
    form_class = DepartmentForm

    def get_success_url(self):
        return reverse_lazy('department_detail', kwargs={'pk': self.object.id})


class DepartmentDeleteView(DeleteView):
    template_name = "department/delete.html"
    model = Department
    success_url = reverse_lazy('department_list')


class ProfessorListView(ListView):
    template_name = "professor/index.html"
    context_object_name = 'professors'

    def get_queryset(self):
        return Professor.objects.all().order_by('last_name')


class ProfessorDetailView(DetailView):
    template_name = "professor/detail.html"
    context_object_name = 'professor'
    model = Professor


class ProfessorUpdateView(UpdateView):
    template_name = "professor/update.html"
    model = Professor
    form_class = ProfessorForm

    def get_success_url(self):
        return reverse_lazy('professor_detail', kwargs={'pk': self.object.id})


class ProfessorCreateView(CreateView):
    template_name = "professor/create.html"
    model = Professor
    form_class = ProfessorForm

    def get_success_url(self):
        return reverse_lazy('professor_detail', kwargs={'pk': self.object.id})


class ProfessorDeleteView(DeleteView):
    template_name = "professor/delete.html"
    model = Professor
    success_url = reverse_lazy('professor_list')


class CourseListView(ListView):
    template_name = "course/index.html"
    context_object_name = 'courses'

    def get_queryset(self):
        return Course.objects.all().order_by('name')


class CourseDetailView(DetailView):
    template_name = "course/detail.html"
    context_object_name = 'course'
    model = Course


class CourseUpdateView(UpdateView):
    template_name = "course/update.html"
    model = Course
    form_class = CourseForm

    def get_success_url(self):
        return reverse_lazy('course_detail', kwargs={'pk': self.object.id})


class CourseCreateView(CreateView):
    template_name = "course/create.html"
    model = Course
    form_class = CourseForm

    def get_success_url(self):
        return reverse_lazy('course_detail', kwargs={'pk': self.object.id})


class CourseDeleteView(DeleteView):
    template_name = "course/delete.html"
    model = Course
    success_url = reverse_lazy('course_list')


class StudentListView(ListView):
    template_name = "student/index.html"
    context_object_name = 'students'

    def get_queryset(self):
        return Student.objects.all().order_by('last_name')


class StudentDetailView(DetailView):
    template_name = "student/detail.html"
    context_object_name = 'student'
    model = Student


class StudentUpdateView(UpdateView):
    template_name = "student/update.html"
    model = Student
    form_class = StudentForm

    def get_success_url(self):
        return reverse_lazy('student_detail', kwargs={'pk': self.object.id})


class StudentCreateView(CreateView):
    template_name = "student/create.html"
    model = Student
    form_class = StudentForm

    def get_success_url(self):
        return reverse_lazy('student_detail', kwargs={'pk': self.object.id})


class StudentDeleteView(DeleteView):
    template_name = "student/delete.html"
    model = Student
    success_url = reverse_lazy('student_list')


class GradeUpdateView(UpdateView):
    template_name = "grade/update.html"
    model = Grade
    form_class = GradeUpdateForm

    def get_success_url(self):
        return reverse_lazy('student_detail', kwargs={'pk': self.object.student.id})


class GradeCreateView(CreateView):
    template_name = "grade/create.html"
    model = Grade
    form_class = GradeCreateForm

    def get_initial(self):
        initial = super().get_initial()
        initial['student'] = get_object_or_404(Student, pk=self.kwargs["student_id"])
        return initial

    def get_context_data(self, **kwargs):
        context  = super().get_context_data(**kwargs)
        context['student'] = get_object_or_404(Student, pk=self.kwargs["student_id"])
        return context

    def get_success_url(self):
        return reverse_lazy('student_detail', kwargs={'pk': self.object.student.id})


class GradeDeleteView(DeleteView):
    template_name = "grade/delete.html"
    model = Grade

    def get_success_url(self):
        return reverse_lazy('student_detail', kwargs={'pk': self.object.student.id})