from django.urls import path
from . import views # views imported from Current directory of workrecords - Peter

urlpatterns = [
    path('employer/<int:pk>/add_employee/employee/<int:emp_pk>/', views.add_an_employee, name='remoodwork-add-employee'),
]