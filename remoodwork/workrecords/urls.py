from django.urls import path
from . import views # views imported from Current directory of workrecords - Peter

urlpatterns = [
    path('', views.home_view, name='remoodwork-home'),
    path('pulsesurvey/', views.pulse_survey_view, name='remoodwork-pulse-survey'),
]