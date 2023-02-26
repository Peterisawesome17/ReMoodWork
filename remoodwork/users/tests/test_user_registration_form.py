from users.forms import UserRegistrationForm
from users.models import User, Employer
from users.tests.test_base import UserTestCaseCounter


class UserRegistrationFormTestCase(UserTestCaseCounter):

    @classmethod
    def setUpClass(cls):
        ''' Sets up tests cases of a valid and invalid data inputs
        for the user registration form shown in register_page.html '''
        super(UserRegistrationFormTestCase, cls).setUpClass()
        correct_data_form = {
            'username': 'johnsmith',
            'password1': 'test123!',
            'password2': 'test123!',
            'full_name': 'John Smith',
            'email': 'johntsmith@gmail.com',
            'company_name': 'Google',
            'job_classification_choice': 'EMPLOYEE'
        }
        cls.correct_form = UserRegistrationForm(data=correct_data_form)

        bad_data_form = {
            'username': 'billysilver',
            'password': 'testname15'
        }
        cls.bad_form = UserRegistrationForm(data=bad_data_form)
        # Used to test out form validation (is_valid) method for UserRegistrationForm.
        create_same_username_data_form = {
            'username': 'johnsmith',
            'password1': 'test123!',
            'password2': 'test123!',
            'full_name': 'Billy Silverstone',
            'email': 'johntsmith@gmail.com',
            'company_name': 'Google',
            'job_classification_choice': 'EMPLOYEE'
        }
        cls.create_same_username_form = UserRegistrationForm(data=create_same_username_data_form)

        create_same_full_name_data_form = {
            'username': 'billysilver',
            'password1': 'testname15',
            'password2': 'testname15',
            'full_name': 'John Smith',
            'email': 'johntsmith@gmail.com',
            'company_name': 'Google',
            'job_classification_choice': 'EMPLOYEE'
        }

        cls.create_same_full_name_form = UserRegistrationForm(data=create_same_full_name_data_form)

        create_employer_data_form = {
            'username': 'jamesjohnson',
            'password1': 'jamestest456!',
            'password2': 'jamestest456!',
            'full_name': 'James S. Johnson',
            'email': 'jamesjohnson@gmail.com',
            'company_name': 'Google',
            'job_classification_choice': 'EMPLOYER'
        }

        cls.create_employer_form = UserRegistrationForm(data=create_employer_data_form)

    def test_valid_form(cls):
        ''' Test 1: A valid test case
        to make sure the correct user registration form is valid before saving
        its data content associated to the model '''
        cls.assertTrue(cls.correct_form.is_valid())

    def test_existed_user(cls):
        ''' Test 2: A valid test case
        to see of a correct user registration form is saved
        for creating a new user stored in a database model record. '''
        cls.correct_form.save()
        cls.assertEqual(1, len(User.objects.all()))
        user1 = User.objects.first()
        cls.assertEqual(cls.correct_form.data.get('username'), user1.username)
        cls.assertTrue(user1.check_password(cls.correct_form.data.get('password1')))
        cls.assertEqual(cls.correct_form.data.get('full_name'), user1.full_name)
        cls.assertEqual(cls.correct_form.data.get('email'), user1.email)
        cls.assertEqual(cls.correct_form.data.get('company_name'), user1.company_name)
        cls.assertEqual(cls.correct_form.data.get('job_classification_choice'),
                        user1.job_classification_choice)

    def test_invalid_bad_form(cls):
        ''' Test 3: An invalid test case
        to see if an invalid user registration form
        is unable to be valid and will not be able to save its data content associated to its
        model. '''
        cls.assertFalse(cls.bad_form.is_valid())

    def test_bad_form(cls):
        ''' Test 4: An invalid test case
        to see if a user registration form provides a prompt
        to user stating that any empty fields must be required to fill in before a user
        gets registered saved through a database model of a software application. '''
        required_field_text = 'This field is required.'
        cls.assertEqual(required_field_text, ''.join(cls.bad_form.errors.get('full_name')))
        cls.assertEqual(required_field_text, ''.join(cls.bad_form.errors.get('email')))
        cls.assertEqual(required_field_text, ''.join(cls.bad_form.errors.get('company_name')))
        cls.assertEqual(required_field_text,
                        ''.join(cls.bad_form.errors.get('job_classification_choice')))
        cls.assertEqual(0, len(User.objects.all()))

    def test_username_already_created(cls):
        ''' Test 5: An invalid test case to see if a username of a user has already been created
        when a user tries to create a new user registration for remoodwork. '''
        cls.correct_form.save()
        cls.assertEqual(1, len(User.objects.all()))
        # Should be invalid due to a username's existence found on the remoodwork's
        # database table
        cls.assertFalse(cls.create_same_username_form.is_valid())
        assert 'A user with that username already exists.' \
               in cls.create_same_username_form.errors.get('username'), 'Username is created again'

    def test_full_name_already_created(cls):
        ''' Test 6: An invalid test case to see if a full name of a user already exists
        when a user tries to create a new user registration for remoodwork.
        '''
        cls.correct_form.save()
        cls.assertEqual(1, len(User.objects.all()))
        cls.assertFalse(cls.create_same_full_name_form.is_valid())
        assert 'A user with that full name already exists.' \
               in cls.create_same_full_name_form.errors.get('full_name'), 'Full name is created again'

    def test_create_employer_form(cls):
        cls.create_employer_form.save()
        cls.assertEqual(1, len(Employer.objects.all()))
        cls.assertEqual(1, len(User.objects.all()))
        user2 = User.objects.first()
        cls.assertEqual(cls.create_employer_form.data.get('username'), user2.username)
        cls.assertTrue(user2.check_password(cls.create_employer_form.data.get('password1')))
        cls.assertEqual(cls.create_employer_form.data.get('full_name'), user2.full_name)
        cls.assertEqual(cls.create_employer_form.data.get('email'), user2.email)
        cls.assertEqual(cls.create_employer_form.data.get('company_name'), user2.company_name)
        cls.assertEqual(cls.create_employer_form.data.get('job_classification_choice'),
                        user2.job_classification_choice)

    @classmethod
    def tearDownClass(cls):
        ''' Invokes teardownClass method from test_base.py file of all
        test suites of the user app for remoodwork. '''
        super().tearDownClass()
