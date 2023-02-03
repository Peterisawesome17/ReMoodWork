from django.urls import path
from . import views # views imported from Current directory of workrecords - Peter

urlpatterns = [
    path('register/', views.register_view, name='remoodwork-users-register'),
]