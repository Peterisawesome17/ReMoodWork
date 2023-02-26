from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    ''' A User model contains about 6 attribute fields needed to be created in the database table
       of remoodwork '''
    CLASSIFICATION_CHOICE = (
        ("EMPLOYEE", 'Employee'),
        ("EMPLOYER", 'Employer')
    )
    # AbstractUser should contain a username and a password attribute
    full_name = models.CharField(max_length=205, verbose_name='full name')
    email = models.EmailField(max_length=205, verbose_name='email')
    company_name = models.CharField(max_length=205, verbose_name='company name')
    job_classification_choice = models.CharField(max_length=10, choices=CLASSIFICATION_CHOICE)

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.full_name}'

class Employer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    employees = models.ManyToManyField(Employee, related_name='employers')

    def __str__(self):
        return f'{self.user.full_name}'

