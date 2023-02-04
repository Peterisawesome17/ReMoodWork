from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

CLASSIFICATION_CHOICE = (
    ("EMPLOYEE", 'Employee'),
    ("EMPLOYER", 'Employer')
)

# job_classification = models.TextChoices("JOBCLASS", "EMPLOYEE EMPLOYER")

class User(AbstractUser):
    # AbstractUser should contain a username and a password attribute
    first_name = models.CharField(max_length=205, verbose_name='first name')
    last_name = models.CharField(max_length=205, verbose_name='last name')
    email = models.EmailField(max_length=205, verbose_name='email')
    company_name = models.CharField(max_length=205, verbose_name='company name')
    job_classification_choice = models.CharField(max_length=10, choices=CLASSIFICATION_CHOICE)

    def save(self, *args, **kwargs):
        # This override method might be useful to save changes of a User model - Peter
        print('Hello save!')
        # super().save(*args, **kwargs)

