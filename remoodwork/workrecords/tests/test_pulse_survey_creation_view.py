from workrecords.tests.test_base import WorkRecordsTestCaseCounter
from users.models import User, Employee
from django.test import Client
from django.urls import reverse
from datetime import date
from workrecords.models import PulseSurvey

class PulseSurveyCreationViewTestCase(WorkRecordsTestCaseCounter):
    @classmethod
    def setUpClass(cls):
        ''' Sets ups test cases on testing view responses of a
        pulse survey creation produced from an employee '''
        cls.user = cls._create_an_employee()
        cls.employee = Employee(user=cls.user)
        cls.employee.save()
        cls.client = Client()

    @classmethod
    def _create_an_employee(cls):
        ''' Sets up an employee creation used for creating and evaluating test
        cases for pulse survey '''
        username = 'adamsmart'
        password = 'anothertest666!'
        full_name = 'Adam Smart'
        email = 'adamsmart@test.com'
        company_name = 'Apple'
        job_classification_choice = 'EMPLOYEE'
        user = User.objects.create_user(
            username=username,
            password=password,
            full_name=full_name,
            email=email,
            company_name=company_name,
            job_classification_choice=job_classification_choice
        )
        return user
    def test_pulse_survey_main_page(cls):
        ''' Test 1: Valid test case for users(employee) responding
        to view their lists of pulse survey (Must be in pulse_survey_main_page.html)'''
        login_response = cls.client.post(reverse('remoodwork-login-user'), {'username': cls.user.username,
                                                                            'password': 'anothertest666!'})
        cls.assertEqual(302, login_response.status_code)
        response = cls.client.get(reverse('remoodwork-pulse-survey',
                                          kwargs={'pk': cls.user.pk}))
        cls.assertEqual(200, response.status_code)
        cls.assertContains(response=response, text='My Pulse Survey Records')
        cls.assertTemplateUsed(response=response,
                               template_name='workrecords/pulse_survey_main_page.html')

    def test_pulse_survey_create_response(cls):
        ''' Test 2: Valid test case for users(employee) responding
        to create their pulse surveys (Must be in create_pulse_survey_page.html) '''
        # response = cls.client.get(cls.create_pulse_survey_url)
        # Must require users to be logged in with their username and password
        login_response = cls.client.post(reverse('remoodwork-login-user'), {'username': cls.user.username,
                                               'password': 'anothertest666!'})
        # Must be redirected successfully
        cls.assertEqual(302, login_response.status_code)

        # Checks if a client can access create_pulse_survey_page.html before creating
        # their pulse surveys
        create_pulse_survey_response = cls.client.get(reverse('remoodwork-create-pulse-survey',
                                          kwargs={'pk':cls.user.pk}))
        csrf_token = create_pulse_survey_response.cookies.get('csrftoken')
        cls.assertEqual(200, create_pulse_survey_response.status_code)
        cls.assertTemplateUsed(response=create_pulse_survey_response,
                               template_name='workrecords/create_pulse_survey_page.html')

        # Must input a sample data to see if a user (employee) can create their pulse surveys
        # and successfully be redirected back to the pulse_survey_main_page.html
        create_pulse_survey_data_form = {
            'activity_name': 'Taco Tuesday',
            'activity_type': 'TB',
            'num_hours': '2',
            'emotional_rate_status': 'taking_break_or_vacation',
            'activity_description': 'Had a blast attending taco party with my coworkers in a '
                                    'breakout room',
            'work_stressor_status': 'NO',
            'activity_created': date.today(),
            'csrfmiddlewaretoken': csrf_token
        }
        pulse_survey_success_created_response = cls.client.post(reverse('remoodwork-create-pulse-survey',
                                          kwargs={'pk':cls.user.pk}),
                                   data=create_pulse_survey_data_form)
        cls.assertNotEqual(200, pulse_survey_success_created_response.status_code)
        cls.assertEqual(302, pulse_survey_success_created_response.status_code)
        cls.assertNotEqual(0, PulseSurvey.objects.all())
        cls.assertRedirects(response=pulse_survey_success_created_response,
                            expected_url=reverse('remoodwork-pulse-survey',
                                          kwargs={'pk':cls.user.pk}))

