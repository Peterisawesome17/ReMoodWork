from django.test import TestCase
from users.models import User, Employee
from users.forms import UserLogInForm
from django.contrib.auth import authenticate

class UserLoginFormTestCase(TestCase):

    @classmethod
    def setUpClass(cls):
        ''' Sets up test cases of a valid and invalid data inputs
        for a user login form showed in the login_page.html. '''
        super(UserLoginFormTestCase, cls).setUpClass()
        # A user model must be created first before invoking a user login
        # form page of remoodwork.
        cls.username = 'jamiesmith'
        cls.password = 'testing123'
        cls.full_name = 'Jamie Smith'
        cls.user1 = User.objects.create_user(username=cls.username, password=cls.password,
                                             full_name=cls.full_name)
        input_user_data_login_cred_form = {
            'username': cls.username,
            'password': cls.password,
        }
        cls.input_user_login_cred_form = UserLogInForm(data=input_user_data_login_cred_form)
        cls.count = 0

    def test_user_created(cls):
        user_created = User.objects.get(username=cls.username)
        cls.assertEqual(cls.user1.username, user_created.username)
        cls.countNum()

    def test_user_authenticated(cls):
        # Must first check if a user input their username and password credentials
        cls.assertTrue(cls.input_user_login_cred_form.is_valid())
        username = cls.input_user_login_cred_form.data.get('username')
        password = cls.input_user_login_cred_form.data.get('password')
        user_authenticated = authenticate(username=username, password=password)
        cls.assertIsNotNone(user_authenticated)
        cls.assertTrue(user_authenticated.is_authenticated)
        cls.assertEqual('Jamie Smith', user_authenticated.full_name)
        cls.countNum()

    def test_invalid_user_authenticated(cls):
        ''' Checks to see if an unregistered user cannot be authenticated
        and have access to their employee/employer profile page in remoodwork'''
        invalid_user_data = {
            'username': 'timtest',
            'password': 'timisthebest123'
        }
        username = invalid_user_data.get('username')
        password = invalid_user_data.get('password')
        user_authenticated = authenticate(username=username, password=password)
        cls.assertIsNone(user_authenticated)
        cls.countNum()

    @classmethod
    def countNum(cls):
        ''' Helper and mutator method to keep counting the number of test cases that were passed
        for a user login page. '''
        cls.count += 1

    @classmethod
    def getNumOfTestCases(cls):
        ''' Helper and a getter method to count a total number of test cases that were passed for a
        user login page. '''
        return cls.count

    @classmethod
    def tearDownClass(cls):
        ''' Used to display the total number of test cases passed with a complete percentage
        number for measuring a test suite of a user login form test cases.
        It also displays the amount of failed test cases presented in the user login
        form test cases. '''
        test_methods = set(test_method for test_method in cls.__dict__ if 'test' in test_method)
        tot_num_test_methods = len(test_methods)
        print(f'Ran {tot_num_test_methods} number of test cases in '
              f'{(cls.getNumOfTestCases() / tot_num_test_methods) * 100}% test suite of {cls.__name__}')
        num_of_failed_test_cases = tot_num_test_methods - cls.getNumOfTestCases()
        if num_of_failed_test_cases:
            print(f'Number of failed test cases occuring {num_of_failed_test_cases}')



