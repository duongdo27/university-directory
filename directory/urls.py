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
]