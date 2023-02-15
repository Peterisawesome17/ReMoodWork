from users.models import User
from users.forms import UserLogInForm
from django.contrib.auth import authenticate
from users.tests.test_base import UserTestCaseCounter

class UserLoginFormTestCase(UserTestCaseCounter):

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

    def test_user_created(cls):
        ''' Test 1: A valid test case to see if a user
        has already been created before running test cases used to
        test out the login page from the user '''
        user_created = User.objects.get(username=cls.username)
        cls.assertEqual(cls.user1.username, user_created.username)

    def test_user_authenticated(cls):
        ''' Test 2: A valid test case to see if a user can
        successfully be authenticated based on the user's existing
        credentials with their username and password as two main attributes
        for a login user story feature '''
        # Must first check if a user input their username and password credentials
        cls.assertTrue(cls.input_user_login_cred_form.is_valid())
        username = cls.input_user_login_cred_form.data.get('username')
        password = cls.input_user_login_cred_form.data.get('password')
        user_authenticated = authenticate(username=username, password=password)
        cls.assertIsNotNone(user_authenticated)
        cls.assertTrue(user_authenticated.is_authenticated)
        cls.assertEqual('Jamie Smith', user_authenticated.full_name)

    def test_invalid_user_authenticated(cls):
        ''' Test 3: An invalid test case to see if an unregistered user cannot be authenticated
        and have access to their survey records or other information in remoodwork '''
        invalid_user_data = {
            'username': 'timtest',
            'password': 'timisthebest123'
        }
        username = invalid_user_data.get('username')
        password = invalid_user_data.get('password')
        user_authenticated = authenticate(username=username, password=password)
        cls.assertIsNone(user_authenticated)

    @classmethod
    def tearDownClass(cls):
        ''' Invokes teardownClass method from test_base.py file of all
        test suites of the user app for remoodwork. '''
        super().tearDownClass()



