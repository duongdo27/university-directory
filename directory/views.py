from django.views.generic import TemplateView
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import UpdateView
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.urls import reverse_lazy

from directory.models import Department
from directory.forms import DepartmentForm
from directory.models import Professor
from directory.forms import ProfessorForm

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
