from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

CLASSIFICATION_CHOICE = (
    ("EMPLOYEE", 'Employee'),
    ("EMPLOYER", 'Employer')
)

# job_classification = models.TextChoices("JOBCLASS", "EMPLOYEE EMPLOYER")

class User(AbstractUser):
    ''' A User model contains about 6 attribute fields needed to be created in the database table
    of remoodwork '''
    # AbstractUser should contain a username and a password attribute
    full_name = models.CharField(max_length=205, verbose_name='full name')
    email = models.EmailField(max_length=205, verbose_name='email')
    company_name = models.CharField(max_length=205, verbose_name='company name')
    job_classification_choice = models.CharField(max_length=10, choices=CLASSIFICATION_CHOICE)



