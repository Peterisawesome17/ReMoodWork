from django.test import TestCase
from users.forms import UserRegistrationForm
from users.models import User


class UserRegistrationFormTestCase(TestCase):

    @classmethod
    def setUpClass(cls):
        ''' Sets up tests cases of a valid and invalid data inputs
        for the user registration form '''
        super(UserRegistrationFormTestCase, cls).setUpClass()
        correct_data_form = {
            'username': 'johnsmith',
            'password': 'test123!',
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
        # cls.create_same_username_form
        cls.count = 0

    def test_valid_form(cls):
        ''' Valid Test Case 1: Check to make sure the correct user registration form is valid
        before saving its data content associated to the model '''
        cls.assertTrue(cls.correct_form.is_valid())
        cls.countNum()

    def test_existed_user(cls):
        ''' Valid Test Case 2: Check to see of a correct user registration form is saved
        and can be used for creating a new user stored in a database model record. '''
        cls.correct_form.save()
        cls.assertEqual(1, len(User.objects.all()))
        user1 = User.objects.first()
        cls.assertEqual(cls.correct_form.data.get('username'), user1.username)
        cls.assertEqual(cls.correct_form.data.get('password'), user1.password)
        cls.assertEqual(cls.correct_form.data.get('full_name'), user1.full_name)
        cls.assertEqual(cls.correct_form.data.get('email'), user1.email)
        cls.assertEqual(cls.correct_form.data.get('company_name'), user1.company_name)
        cls.assertEqual(cls.correct_form.data.get('job_classification_choice'),
                        user1.job_classification_choice)
        cls.countNum()

    def test_invalid_form(cls):
        ''' Invalid test case 1: Checks to see if an invalid user registration form
        is unable to be valid and will not be able to save its data content associated to its
        model. '''
        cls.assertFalse(cls.bad_form.is_valid())
        cls.countNum()

    def test_bad_form(cls):
        ''' Invalid test case 2: Checks to see if a user registration form provides a prompt
        to user stating that any empty fields must be required to fill in before a user
        gets registered saved through a database model of a software application. '''
        required_field_text = 'This field is required.'
        cls.assertEqual(required_field_text, ''.join(cls.bad_form.errors.get('full_name')))
        cls.assertEqual(required_field_text, ''.join(cls.bad_form.errors.get('email')))
        cls.assertEqual(required_field_text, ''.join(cls.bad_form.errors.get('company_name')))
        cls.assertEqual(required_field_text,
                        ''.join(cls.bad_form.errors.get('job_classification_choice')))
        cls.assertEqual(0, len(User.objects.all()))
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
              f'{(cls.getNumOfTestCases() / tot_num_test_methods) * 100}% test suite of {cls.__name__}')
        num_of_failed_test_cases = tot_num_test_methods - cls.getNumOfTestCases()
        if num_of_failed_test_cases:
            print(f'Number of failed test cases occuring {num_of_failed_test_cases}')
