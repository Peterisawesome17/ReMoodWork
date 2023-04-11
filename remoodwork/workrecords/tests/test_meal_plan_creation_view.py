from workrecords.tests.test_base import WorkRecordsTestCaseCounter
from users.models import User, Employee
from django.test import Client
from django.urls import reverse
from workrecords.models import MealPlan


class MealPlanCreationView(WorkRecordsTestCaseCounter):

    @classmethod
    def setUpClass(cls):
        ''' Sets up test cases on testing view responses of a meal planning creation
        produced from an employee '''
        cls.user = cls._create_an_employee()
        cls.employee = Employee(user=cls.user)
        cls.employee.save()
        cls.client = Client()

    def test_pulse_survey_main_page(cls):
        ''' Test 1: Valid test case for users(employee) responding to view
        their meal plan assessment plans (Must be in meal_plan_main_page.html) '''
        login_response = cls.client.post(reverse('remoodwork-login-user'), {'username': cls.user.username,
                                                                            'password': 'anothertest666!'})
        cls.assertEqual(302, login_response.status_code)
        response = cls.client.get(reverse('remoodwork-meal-plan', kwargs={'pk': cls.user.pk}))
        cls.assertEqual(200, response.status_code)
        cls.assertContains(response=response, text='My Meal Plan Records')
        cls.assertTemplateUsed(response=response,
                               template_name='workrecords/meal_plan_main_page.html')


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




