from workrecords.tests.test_base import WorkRecordsTestCaseCounter
from users.models import User, Employer
from django.test import Client
from django.urls import reverse
from workrecords.models import FoodItem

class FoodItemandOrderCreationViewTestCase(WorkRecordsTestCaseCounter):
    @classmethod
    def setUpClass(cls):
        ''' Sets up test cases on testing view responses of a food item creation
        produced from an employer '''
        cls.user = cls._create_an_user()
        cls.employer = Employer(user=cls.user)
        cls.employer.save()
        cls.client = Client()

    def test_food_item_create_response(cls):
        ''' Test 1: Valid test case for users(employers) responding
        to create food item (Must be in create_food_item_page.html) '''
        login_response = cls.client.post(reverse('remoodwork-login-user'),
                                         {'username': cls.user.username,
                                          'password': 'anothertest666!'})
        cls.assertEqual(302, login_response.status_code)
        cls.assertRedirects(login_response, reverse('remoodwork-home'))
        create_food_item_response = cls.client.get(reverse('remoodwork-create-food-item',
                                                           kwargs={'emp_pk': cls.employer.user.pk}))
        csrf_token = create_food_item_response.cookies.get('csrftoken')
        cls.assertIsNotNone(csrf_token)
        cls.assertEqual(200, create_food_item_response.status_code)
        cls.assertTemplateUsed(response=create_food_item_response,
                               template_name='workrecords/create_food_item_page.html')
        create_food_item_restaurant_data_form = {
            'food_name': 'Smoked salmon',
            'description': 'Cooked and marinated with lemon juice',
            'price': 20.00,
            'cuisine_type': 'american',
            'food_item_type': 'restaurant',
            'restaurant_name': 'Dr.Dock\'s Seafood Restaurant',
            'calories': 200,
            'dietary_restrictions': 'gluten-free',
            'allergy': 'shellfish',
            'csrfmiddlewaretoken': csrf_token
        }

        food_item_restaurant_created_response = cls.client.post(
            reverse('remoodwork-create-food-item',kwargs={'emp_pk': cls.employer.user.pk}),
        data=create_food_item_restaurant_data_form)

        cls.assertEqual(302, food_item_restaurant_created_response.status_code)
        cls.assertNotEqual(200, food_item_restaurant_created_response.status_code)
        cls.assertEqual(1, len(FoodItem.objects.all()))
        cls.assertRedirects(response=food_item_restaurant_created_response,
                            expected_url=reverse('remoodwork-home'))
        food_item_in_home_page_response = cls.client.get(reverse('remoodwork-home'))
        cls.assertEqual(200, food_item_in_home_page_response.status_code)
