from users.tests.test_base import UserTestCaseCounter
from users.models import User, Employee, Employer
from django.test import Client
from django.urls import reverse



class UsersViewTestCase(UserTestCaseCounter):
    @classmethod
    def setUpClass(cls):
        ''' Sets up test cases testing users response through
        their registration, login, and logout process '''
        # Users must be registered first before evaluating test cases with login/logout
        cls.client = Client()
        cls.register_data = {
            'username': 'johnsmith',
            'password1': 'test123!',
            'password2': 'test123!',
            'full_name': 'John Smith',
            'email': 'johntsmith@gmail.com',
            'company_name': 'Google',
            'job_classification_choice': 'EMPLOYEE'
        }
        cls.register_employer_data = {
            'username': 'jamesjohnson',
            'password1': 'jamestest456!',
            'password2': 'jamestest456!',
            'full_name': 'James S. Johnson',
            'email': 'jamesjohnson@gmail.com',
            'company_name': 'Google',
            'job_classification_choice': 'EMPLOYER'
        }

    def test_user_registration_view(cls):
        ''' Test 1: Valid test case to see if a user(employee for now)
        can register their account in the registration view page of remoodwork'''
        # Checks to see if there is a csrf_token value found in the registration page of remoodwork
        response = cls.client.get(reverse('remoodwork-register-user'))
        csrf_token = response.cookies.get('csrftoken')
        cls.assertIsNotNone(csrf_token)
        cls.assertEqual(200, response.status_code)
        cls.assertTemplateUsed(response=response,
                               template_name='users/register_page.html')
        # Checks if a user is able to successfully register their account from a registration
        # view page of remoodwork
        user_registration_response = cls.client.post(reverse('remoodwork-register-user'),
                                                     data=cls.register_data | {'csrfmiddlewaretoken':csrf_token})
        cls.assertNotEqual(200, user_registration_response.status_code)
        cls.assertEqual(302, user_registration_response.status_code)
        # User and Employee should be able to have one user after successfully registering
        # their account through remoodwork
        cls.assertEqual(1, len(User.objects.all()))
        cls.assertEqual(1, len(Employee.objects.all()))
        # Users should be able to be redirected back to the home page of remoodwork
        # after successfully registering their account
        cls.assertRedirects(response=user_registration_response,
                            expected_url=reverse('remoodwork-home'))

    def test_user_login_and_logout_view(cls):
        ''' Test 2: Valid test case to see if a user(employee for now)
        can be logged in and out with their account credentials (username and password) '''
        cls.assertEqual(0, len(User.objects.all()))
        response = cls.client.get(reverse('remoodwork-register-user'))
        csrf_token = response.cookies.get('csrftoken')
        user_registration_response = cls.client.post(reverse('remoodwork-register-user'),
                                                     data=cls.register_data | {'csrfmiddlewaretoken': csrf_token})
        # User and Employee should be able to have one user after successfully registering
        # their account through remoodwork
        cls.assertEqual(1, len(User.objects.all()))
        cls.assertEqual(1, len(Employee.objects.all()))

        # Checks if a user(employee) is able to login with their username and password credentials
        # after registering their account
        login_display_reponse = cls.client.get(reverse('remoodwork-login-user'))
        cls.assertTemplateUsed(response=login_display_reponse,
                               template_name='users/login_page.html')
        login_response = cls.client.post(reverse('remoodwork-login-user'),
                                         {'username': 'johnsmith', 'password': 'test123!'})
        cls.assertEqual(302, login_response.status_code)
        cls.assertRedirects(response=login_response,
                            expected_url=reverse('remoodwork-home'))
        # Creating pulse surveys is one of the examples that should be able to verify
        # if a user is able to successfully be logged in that has employee's access to the pages of remoodwork
        # (except admin page)
        user = User.objects.get(username='johnsmith')
        create_pulse_survey_response = cls.client.get(reverse('remoodwork-create-pulse-survey',
                                                              kwargs={'pk': user.pk}))
        cls.assertEqual(200, create_pulse_survey_response.status_code)

        # Checks if a user(employee) is able to logout and cannot access some pages in remoodwork
        logout_response = cls.client.post(reverse('remoodwork-logout-user'),
                                          {'username': 'johnsmith', 'password': 'test123!'})
        cls.assertEqual(200, logout_response.status_code)
        cls.assertTemplateUsed(response=logout_response,
                               template_name='users/logout_page.html')
        # Should be able to raise Exceptions on creating a pulse survey (as an example)
        # due to the logout process from the user's credentials (username and password)
        with cls.assertRaises(Exception):
            cls.client.get(reverse('remoodwork-create-pulse-survey', kwargs={'pk': user.pk}))

    def test_register_employer_view(cls):
        ''' Test 3: Valid test case to see if an employer
        can register their account in a registration view page of remoodwork '''
        response = cls.client.get(reverse('remoodwork-register-user'))
        csrf_token = response.cookies.get('csrftoken')
        cls.assertIsNotNone(csrf_token)
        cls.assertEqual(200, response.status_code)
        cls.assertTemplateUsed(response=response,
                               template_name='users/register_page.html')
        # Checks if a user is able to successfully register their account from a registration
        # view page of remoodwork
        employer_registration_response = cls.client.post(reverse('remoodwork-register-user'),
                                                     data=cls.register_employer_data | {'csrfmiddlewaretoken': csrf_token})
        cls.assertNotEqual(200, employer_registration_response.status_code)
        cls.assertEqual(302, employer_registration_response.status_code)
        # User and Employer should be able to have one user after successfully registering
        # their account through remoodwork
        cls.assertEqual(1, len(User.objects.all()))
        cls.assertEqual(1, len(Employer.objects.all()))
        # Users should be able to be redirected back to the home page of remoodwork
        # after successfully registering their account
        cls.assertRedirects(response=employer_registration_response,
                            expected_url=reverse('remoodwork-home'))


