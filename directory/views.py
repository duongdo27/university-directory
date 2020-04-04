from django.views.generic import TemplateView
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import UpdateView
from django.views.generic import CreateView
from django.urls import reverse_lazy

from directory.models import Department
from directory.forms import DepartmentForm


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
    context_object_name = 'department'
    model = Department
    form_class = DepartmentForm

    def get_success_url(self):
        return reverse_lazy('department_detail', kwargs={'pk': self.object.id})


class DepartmentCreateView(CreateView):
    template_name = "department/create.html"
    context_object_name = 'department'
    model = Department
    form_class = DepartmentForm

    def get_success_url(self):
        return reverse_lazy('department_detail', kwargs={'pk': self.object.id})
