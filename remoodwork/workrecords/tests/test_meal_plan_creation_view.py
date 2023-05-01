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
        cls.user = cls._create_an_user()
        cls.employee = Employee(user=cls.user)
        cls.employee.save()
        cls.client = Client()

    def test_meal_plan_main_page(cls):
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

    def test_meal_plan_create_response(cls):
        '''Test 2: Valid test case for users(employees) responding
        to create their meal plan (Must be in create_meal_plan_page.html) '''
        login_response = cls.client.post(reverse('remoodwork-login-user'), {'username': cls.user.username,
                                               'password': 'anothertest666!'})
        cls.assertEqual(302, login_response.status_code)
        create_meal_plan_response = cls.client.get(reverse('remoodwork-create-meal-plan',
                                                           kwargs={'pk':cls.user.pk}))
        csrf_token = create_meal_plan_response.cookies.get('csrftoken')
        cls.assertIsNotNone(csrf_token)
        cls.assertEqual(200, create_meal_plan_response.status_code)
        cls.assertTemplateUsed(response=create_meal_plan_response,
                               template_name='workrecords/create_meal_plan_page.html')
        create_meal_plan_data_form = {
            "calories": 300,
            "dietary_restrictions": "gluten-free",
            "goal": "To lose weight by 30 lbs",
            "allergy": "wheat",
            "budget": 20.00,
            "cuisine": "American",
            'csrfmiddlewaretoken': csrf_token
        }

        meal_plan_created_response = cls.client.post(reverse('remoodwork-create-meal-plan',
                                                             kwargs={'pk': cls.user.pk}),
                                                     data=create_meal_plan_data_form)
        #Must redirect back to a meal plan main page
        cls.assertEqual(302, meal_plan_created_response.status_code)
        cls.assertNotEqual(200, meal_plan_created_response.status_code)
        cls.assertNotEqual(0, len(MealPlan.objects.all()))
        cls.assertRedirects(response=meal_plan_created_response,
                            expected_url=reverse('remoodwork-meal-plan', kwargs={'pk':cls.user.pk}),
                            )
        create_meal_plan_response_2 = cls.client.get(reverse('remoodwork-meal-plan',
                                                           kwargs={'pk': cls.user.pk}))
        cls.assertContains(response=create_meal_plan_response_2,
                           text='Calories: 300')
        cls.assertContains(create_meal_plan_response_2, "Dietary restrictions: gluten-free")
        cls.assertContains(create_meal_plan_response_2, "Food allergies: wheat")
        cls.assertContains(create_meal_plan_response_2, "Food budget: 20.0")
        cls.assertContains(create_meal_plan_response_2, "Cuisines")
        cls.assertContains(create_meal_plan_response_2, "American")
        cls.assertContains(create_meal_plan_response_2, "Goal: To lose weight by 30 lbs")

        meal_plan_on_home_page_response = cls.client.get(reverse('remoodwork-home',
                                                             kwargs={}))
        cls.assertContains(meal_plan_on_home_page_response, "Dietary restrictions: gluten-free")
        cls.assertContains(meal_plan_on_home_page_response, "Food allergies: wheat")
        cls.assertContains(meal_plan_on_home_page_response, "Food budget: 20.0")
        cls.assertContains(meal_plan_on_home_page_response, "Cuisines")
        cls.assertContains(meal_plan_on_home_page_response, "American")
        cls.assertContains(meal_plan_on_home_page_response, "Goal: To lose weight by 30 lbs")




