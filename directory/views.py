from django.views.generic import TemplateView
from django.views.generic import ListView
from django.views.generic import DetailView

from directory.models import Department


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



