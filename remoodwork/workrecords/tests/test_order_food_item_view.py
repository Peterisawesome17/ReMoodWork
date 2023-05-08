from workrecords.tests.test_base import WorkRecordsTestCaseCounter
from users.models import Employer, Employee, User
from workrecords.models import FoodItem, MealPlan, Order
from django.urls import reverse
from django.test import Client


class OrderFoodItemViewTestCase(WorkRecordsTestCaseCounter):
    @classmethod
    def setUpClass(cls):
        super(WorkRecordsTestCaseCounter, cls).setUpClass()
        cls.employer = cls._create_an_employer()
        cls.employer.save()
        cls.employee = cls._create_an_employee()
        cls.employee.save()
        cls.meal_plan = cls._create_meal_plan(cls.employee)
        cls.meal_plan.save()
        cls.food_item = cls._create_food_item_1(cls.employer)
        cls.food_item.save()
        cls.another_food_item = cls._create_food_item_2(cls.employer)
        cls.another_food_item.save()
        cls.client = Client()
        assert 1 == len(Employee.objects.all()), 'No employee created'
        assert 1 == len(Employer.objects.all()), 'No employer created'
        assert 1 == len(MealPlan.objects.all()), 'No meal plan created'
        assert 2 == len(FoodItem.objects.all()), 'No food meal items created'

    def test_order_meal_response(cls):
        ''' Test 1: Valid test case for the system filtering food meal items
        based on employee's meal planning and allows employees to select and order
        their food meal item. '''
        login_response = cls.client.post(reverse('remoodwork-login-user'),
                                         {'username': cls.employee.user.username,
                                          'password': 'anothertest555!'})
        cls.assertEqual(302, login_response.status_code)
        cls.assertRedirects(login_response, reverse('remoodwork-home'))
        meal_plan_page_response = cls.client.get(reverse("remoodwork-meal-plan",
                                                         kwargs={'pk': cls.employee.user.pk}))
        cls.assertEqual(200, meal_plan_page_response.status_code)
        cls.assertNotContains(meal_plan_page_response, 'Already selected this meal')
        cls.assertContains(meal_plan_page_response, "Meal choices that are recommended for you")
        cls.assertContains(meal_plan_page_response, '/media/meal_item_images/Example_Salmon')
        cls.assertContains(meal_plan_page_response, "Food name: Smoked Salmon")
        cls.assertContains(meal_plan_page_response, "Description: Cooked and marinated with lemon juice")
        cls.assertContains(meal_plan_page_response, "Price: 20.0")
        cls.assertContains(meal_plan_page_response, "Cuisine: American")
        cls.assertContains(meal_plan_page_response, "Type: Restaurant")
        cls.assertContains(meal_plan_page_response, "Restaurant name: Dr.Dock")
        cls.assertContains(meal_plan_page_response, "Calories: 200")
        cls.assertContains(meal_plan_page_response, "Dietary Restrictions: Gluten-free")
        cls.assertContains(meal_plan_page_response, "Allergy: Soy")
        cls.assertContains(meal_plan_page_response, "Food name: Texas-Style Beef Brisket")
        cls.assertContains(meal_plan_page_response, "Recipe Link")
        cls.assertContains(meal_plan_page_response, "Type: Recipe")
        cls.assertContains(meal_plan_page_response, "Select")
        #Check if another food meal item has no image represented as default.jpg
        cls.assertContains(meal_plan_page_response, "/media/default.jpg")
        order_meal_response = cls.client.get(reverse('remoodwork-order-meal',
                                                     kwargs={'pk': cls.employee.user.pk,
                                                             'food_pk': cls.food_item.pk}))
        cls.assertEqual(200, order_meal_response.status_code)
        cls.assertContains(order_meal_response, 'Do you want to order this meal Smoked Salmon')
        cls.assertContains(order_meal_response, '/media/meal_item_images/Example_Salmon')
        order_meal_created_reponse = cls.client.post(reverse('remoodwork-order-meal',
                                                     kwargs={'pk': cls.employee.user.pk,
                                                             'food_pk': cls.food_item.pk}),
                                                     {'order_meal': 'yes'})
        cls.assertEqual(302, order_meal_created_reponse.status_code)
        cls.assertEqual(1, len(Order.objects.all()))
        meal_plan_page_response = cls.client.get(reverse("remoodwork-meal-plan",
                                                         kwargs={'pk': cls.employee.user.pk}))
        cls.assertEqual(200, meal_plan_page_response.status_code)
        cls.assertContains(meal_plan_page_response, 'Already selected this meal')





