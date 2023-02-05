from django.test import TestCase
from users.forms import UserRegistrationForm
from users.models import User


class UserRegistrationFormTestCase(TestCase):

    @classmethod
    def setUpClass(cls):
        super(UserRegistrationFormTestCase, cls).setUpClass()
        correct_data_form = {
            'username': 'johnsmith',
            'password': 'test123!',
            'first_name': 'John',
            'last_name': 'Smith',
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
        cls.count = 0

    def test_valid_form(cls):
        cls.assertTrue(cls.correct_form.is_valid())
        cls.countNum()

    def test_existed_user(cls):
        cls.correct_form.save()
        cls.assertEqual(1, len(User.objects.all()))
        user1 = User.objects.first()
        cls.assertEqual(cls.correct_form.data.get('username'), user1.username)
        cls.assertEqual(cls.correct_form.data.get('password'), user1.password)
        cls.assertEqual(cls.correct_form.data.get('first_name'), user1.first_name)
        cls.assertEqual(cls.correct_form.data.get('last_name'), user1.last_name)
        cls.assertEqual(cls.correct_form.data.get('email'), user1.email)
        cls.assertEqual(cls.correct_form.data.get('company_name'), user1.company_name)
        cls.assertEqual(cls.correct_form.data.get('job_classification_choice'),
                        user1.job_classification_choice)
        cls.countNum()

    def test_invalid_form(cls):
        cls.assertFalse(cls.bad_form.is_valid())
        cls.countNum()

    def test_bad_form(cls):
        required_field_text = 'This field is required.'
        cls.assertEqual(required_field_text, ''.join(cls.bad_form.errors.get('first_name')))
        cls.assertEqual(required_field_text, ''.join(cls.bad_form.errors.get('last_name')))
        cls.assertEqual(required_field_text, ''.join(cls.bad_form.errors.get('email')))
        cls.assertEqual(required_field_text, ''.join(cls.bad_form.errors.get('company_name')))
        cls.assertEqual(required_field_text,
                        ''.join(cls.bad_form.errors.get('job_classification_choice')))
        cls.assertEqual(0, len(User.objects.all()))
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
              f'{(cls.getNumOfTestCases() / tot_num_test_methods) * 100}% test suite of {cls.__name__}')
        num_of_failed_test_cases = tot_num_test_methods - cls.getNumOfTestCases()
        if num_of_failed_test_cases:
            print(f'Number of failed test cases occuring {num_of_failed_test_cases}')
