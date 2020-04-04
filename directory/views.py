from django.views.generic import TemplateView
from django.views.generic import ListView

from directory.models import Department


class IndexView(TemplateView):
    template_name = "index.html"


class DepartmentListView(ListView):
    template_name = "department/index.html"
    context_object_name = 'departments'

    def get_queryset(self):
        return Department.objects.all().order_by('name')

