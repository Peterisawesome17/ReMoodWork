from django.test import TestCase
import os, django
from users.models import User, CLASSIFICATION_CHOICE


# Create your tests here.
class UserModelTestCases(TestCase):
    @classmethod
    def setUpClass(cls):
        ''' Sets up test cases of creating a new User model and
        fetching its provided data of the User. '''
        super(UserModelTestCases, cls).setUpClass()
        cls.username = 'johnsmith'
        cls.password = 'test123!'
        cls.full_name = 'John Smith'
        cls.email = 'johntsmith@gmail.com'
        cls.company_name = 'Google'
        cls.job_classification_choice = 'EMPLOYEE'
        cls.user1 = User(
            username=cls.username,
            password=cls.password,
            full_name=cls.full_name,
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
        ''' Tests an existing username already created. '''
        cls.assertEqual(cls.username, cls.user1.username)
        cls.countNum()

    def test_password(cls):
        ''' Tests an existing password already created. '''
        cls.assertEqual(cls.password, cls.user1.password)
        cls.countNum()

    def test_full_name(cls):
        ''' Tests an existing full name already created. '''
        cls.assertEqual(cls.full_name, cls.user1.full_name)
        cls.countNum()

    def test_email(cls):
        ''' Tests an existing email already created. '''
        cls.assertEqual(cls.email, cls.user1.email)
        cls.countNum()

    def test_company_name(cls):
        '''Tests an existing company name already created. '''
        cls.assertEqual(cls.company_name, cls.user1.company_name)
        cls.countNum()

    def test_job_classification_choice(cls):
        '''Tests to see if a job classification status of a user is already created. '''
        cls.assertEqual(cls.job_classification_choice, cls.user1.job_classification_choice)
        cls.countNum()

    def test_user_existence(cls):
        '''Tests to see if a new user is created in a user model of remoodwork system. '''
        userslst = User.objects.all().filter(pk=1)
        dummy_user = userslst[0]
        cls.assertEqual(dummy_user, cls.user1)
        cls.countNum()

    @classmethod
    def countNum(cls):
        ''' Helper and mutator method to keep counting the number of test cases that were passed
                for a user registration page. '''
        cls.count += 1
    @classmethod
    def getNumOfTestCases(cls):
        ''' Helper and a getter method to count a total number of test cases that were passed for a
               user registration page. '''
        return cls.count

    @classmethod
    def tearDownClass(cls):
        ''' Used to display the total number of test cases passed with a complete percentage
                number for measuring a test suite of a user registration form test cases.
                It also displays the amount of failed test cases presented in the user registration
                form test cases. '''
        test_methods = set(test_method for test_method in cls.__dict__ if 'test' in test_method)
        tot_num_test_methods = len(test_methods)
        print(f'Ran {tot_num_test_methods} number of test cases in '
              f'{(cls.getNumOfTestCases()/tot_num_test_methods) * 100}% test suite of {cls.__name__}')
        num_of_failed_test_cases = tot_num_test_methods-cls.getNumOfTestCases()
        if num_of_failed_test_cases:
            print(f'Number of failed test cases occuring {num_of_failed_test_cases}')


