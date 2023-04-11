from django.urls import path
from . import views # views imported from Current directory of workrecords - Peter

urlpatterns = [
    path('', views.home_view, name='remoodwork-home'),
    path('employee/<int:pk>/pulsesurvey/', views.pulse_survey_view, name='remoodwork-pulse-survey'),
    path('employee/<int:pk>/pulsesurvey/employer/<int:emp_pk>/', views.pulse_survey_view, name='remoodwork-pulse-survey'),
    path('employee/<int:pk>/createpulsesurvey/', views.create_pulse_survey_view, name='remoodwork-create-pulse-survey'),
    path('employee/<int:pk>/mealplan/', views.meal_plan_view, name='remoodwork-meal-plan'),
    path('employee/<int:pk>/createmealplan/', views.create_meal_plan_view, name='remoodwork-create-meal-plan')
]