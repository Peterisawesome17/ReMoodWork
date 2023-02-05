from django.test import TestCase
import os, django
from users.models import User, CLASSIFICATION_CHOICE


# Create your tests here.
class UserModelTestCases(TestCase):
    @classmethod
    def setUpClass(cls):
        super(UserModelTestCases, cls).setUpClass()
        cls.username = 'johnsmith'
        cls.password = 'test123!'
        cls.first_name = 'John'
        cls.last_name = 'Smith'
        cls.email = 'johntsmith@gmail.com'
        cls.company_name = 'Google'
        cls.job_classification_choice = 'EMPLOYEE'
        cls.user1 = User(
            username=cls.username,
            password=cls.password,
            first_name=cls.first_name,
            last_name=cls.last_name,
            email=cls.email,
            company_name=cls.company_name,
            job_classification_choice=cls.job_classification_choice
        )
        cls.user1.save()
        cls.count = 0

    def test_all_user_model(cls):
        ''' Tests all the user models created in the remoodwork/default database tables'''
        cls.assertEqual(1, len(User.objects.all()))
        cls.countNum()

    def test_username(cls):
        cls.assertEqual(cls.username, cls.user1.username)
        cls.countNum()

    def test_password(cls):
        cls.assertEqual(cls.password, cls.user1.password)
        cls.countNum()

    def test_first_name(cls):
        cls.assertEqual(cls.first_name, cls.user1.first_name)
        cls.countNum()

    def test_last_name(cls):
        cls.assertEqual(cls.last_name, cls.user1.last_name)
        cls.countNum()

    def test_email(cls):
        cls.assertEqual(cls.email, cls.user1.email)
        cls.countNum()

    def test_company_name(cls):
        cls.assertEqual(cls.company_name, cls.user1.company_name)
        cls.countNum()

    def test_job_classification_choice(cls):
        cls.assertEqual(cls.job_classification_choice, cls.user1.job_classification_choice)
        cls.countNum()

    def test_filter_user(cls):
        userslst = User.objects.all().filter(pk=1)
        dummy_user = userslst[0]
        cls.assertEqual(dummy_user, cls.user1)
        cls.countNum()

    @classmethod
    def countNum(cls):
        cls.count += 1
    @classmethod
    def getNumOfTestCases(cls):
        return cls.count

    @classmethod
    def tearDownClass(cls):
        test_methods = set(test_method for test_method in cls.__dict__ if 'test' in test_method)
        tot_num_test_methods = len(test_methods)
        print(f'Ran {tot_num_test_methods} number of test cases in '
              f'{(cls.getNumOfTestCases()/tot_num_test_methods) * 100}% test suite of {cls.__name__}')
        num_of_failed_test_cases = tot_num_test_methods-cls.getNumOfTestCases()
        if num_of_failed_test_cases:
            print(f'Number of failed test cases occuring {num_of_failed_test_cases}')


