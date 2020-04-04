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
]