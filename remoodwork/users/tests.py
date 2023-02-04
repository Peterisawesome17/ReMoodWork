from django.test import TestCase
import os, django
from users.models import User, CLASSIFICATION_CHOICE


# Create your tests here.
class UserModelTestCases(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.username = 'johnsmith'
        cls.password = 'test123!'
        cls.first_name = 'John'
        cls.last_name = 'Smith'
        cls.email = 'johntsmith@gmail.com'
        cls.company_name = 'Google'
        cls.job_classification_choice = 'EMPLOYEE'

    def test_all_user_model(cls):
        ''' Tests all the user models created in the remoodwork database tables'''
        print(User.objects.all())
        cls.assertEqual(0, len(User.objects.all()))


