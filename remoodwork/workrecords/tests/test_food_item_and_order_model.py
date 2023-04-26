from users.models import User, Employer, Employee
from workrecords.tests.test_base import WorkRecordsTestCaseCounter
from workrecords.models import FoodItem, MealPlan, Order
import re
from django.db.models import Q

class FoodItemandOrderTestCase(WorkRecordsTestCaseCounter):
    @classmethod
    def setUpClass(cls):
        ''' Sets up test cases for creating a food item made by an employer
        where it shall be allowed to create one or more food items on remoodwork website '''
        super(WorkRecordsTestCaseCounter, cls).setUpClass()
        cls.employer = cls._create_an_employer()
        cls.employer.save()
        cls.employee = cls._create_an_employee()
        cls.employee.save()
        cls.food_item_start = cls._create_food_item(cls.employer)
        cls.food_item_start.save()


    @classmethod
    def _create_food_item(cls, employer):
        ''' Sets up the first food item to make some test cases used in this script '''
        if employer:
            food_name = 'Smoked Salmon'
            description = 'Cooked and marinated with lemon juice'
            price = 20.00
            cuisine_type = 'american'
            food_item_type = 'restaurant'
            restaurant_name = 'Dr.Dock\'s Seafood Restaurant'
            calories = 200
            dietary_restrictions = 'gluten-free'
            allergy = 'soy'
            food_item = FoodItem(
                food_name=food_name,
                description=description,
                price=price,
                cuisine_type=cuisine_type,
                food_item_type=food_item_type,
                restaurant_name=restaurant_name,
                calories=calories,
                dietary_restrictions=dietary_restrictions,
                allergy=allergy,
                employer=employer
            )
            return food_item


    @classmethod
    def _create_food_item_1(cls, employer):
        ''' Sets up the first food item to make some test cases used in this script '''
        if employer:
            food_name = 'Ribeye Steak'
            description = 'This steak is cooked with medium-rare and provides cilantro spices' \
                          'and buttery flavor.'
            price = 50.00
            cuisine_type = 'american'
            food_item_type = 'restaurant'
            restaurant_name = 'Jim Steakhouse Restaurant'
            calories = 300
            dietary_restrictions = 'gluten-free'
            allergy = 'beef'
            food_item = FoodItem(
                food_name=food_name,
                description=description,
                price=price,
                cuisine_type=cuisine_type,
                food_item_type=food_item_type,
                restaurant_name=restaurant_name,
                calories=calories,
                dietary_restrictions=dietary_restrictions,
                allergy=allergy,
                employer=employer
            )
            return food_item

    def _create_food_item_2(cls, employer):
        if employer:
            food_name = 'Carne Asada'
            description = 'This recipe will be good if you are a meat lover'
            cuisine_type = 'mexican'
            food_item_type = 'recipe'
            recipe_url = 'https://loseweightbyeating.com/carne-asada-recipe/'
            calories = 250
            dietary_restrictions = 'gluten-free'
            allergy = 'beef'
            food_item = FoodItem(
                food_name=food_name,
                description=description,
                cuisine_type = cuisine_type,
                food_item_type = food_item_type,
                recipe_url = recipe_url,
                calories = calories,
                dietary_restrictions = dietary_restrictions,
                allergy = allergy,
                employer=employer
            )
            return food_item


    def test_an_employer(cls):
        cls.assertNotEqual(0, len(Employer.objects.all()))

    def test_food_item_model_1(cls):
        food_item = cls._create_food_item_1(cls.employer)
        food_item.save()
        cls.assertNotEqual(0, len(FoodItem.objects.all()))
        food_item_match = FoodItem.objects.get(restaurant_name='Jim Steakhouse Restaurant')
        cls.assertIsNotNone(food_item_match)
        cls.assertEqual(food_item.food_name, food_item_match.food_name)
        cls.assertEqual(food_item.description, food_item_match.description)
        cls.assertEqual(food_item.price, food_item_match.price)
        cls.assertEqual(food_item.cuisine_type, food_item_match.cuisine_type)
        cls.assertEqual(food_item.food_item_type, food_item_match.food_item_type)
        cls.assertIsNone(food_item.recipe_url)
        cls.assertEqual(food_item.restaurant_name, food_item_match.restaurant_name)
        cls.assertEqual(food_item.calories, food_item_match.calories)
        cls.assertEqual(food_item.dietary_restrictions, food_item_match.dietary_restrictions)
        cls.assertEqual(food_item.allergy, food_item_match.allergy)
        cls.assertEqual(food_item.employer, food_item_match.employer)

    def test_food_item_model_2(cls):
        food_item = cls._create_food_item_2(cls.employer)
        food_item.save()
        cls.assertNotEqual(0, len(FoodItem.objects.all()))
        food_item_match = FoodItem.objects.get(food_name='Carne Asada')
        cls.assertIsNotNone(food_item_match)
        cls.assertEqual(food_item.food_name, food_item_match.food_name)
        cls.assertEqual(food_item.description, food_item_match.description)
        cls.assertIsNone(food_item.price)
        cls.assertEqual(food_item.cuisine_type, food_item_match.cuisine_type)
        cls.assertEqual(food_item.food_item_type, food_item_match.food_item_type)
        cls.assertEqual(food_item.recipe_url, food_item_match.recipe_url)
        cls.assertIsNone(food_item.restaurant_name)
        cls.assertEqual(food_item.calories, food_item_match.calories)
        cls.assertEqual(food_item.dietary_restrictions, food_item_match.dietary_restrictions)
        cls.assertEqual(food_item.allergy, food_item_match.allergy)
        cls.assertEqual(food_item.employer, food_item_match.employer)

    def _create_meal_plan(cls, employee=None):
        meal_plan = None
        if employee:
            cls.calories = 250
            cls.dietary_restrictions = 'Gluten-free, vegetarian'
            cls.goal = 'To lose weight by 30 lbs'
            cls.allergy = 'Wheat, peanuts, shellfish'
            cls.budget = 20.00
            cls.cuisine = 'American, mexican'
            meal_plan = MealPlan(
                calories=cls.calories,
                dietary_restrictions=cls.dietary_restrictions,
                goal=cls.goal,
                allergy=cls.allergy,
                budget=cls.budget,
                cuisine=cls.cuisine,
                employee=employee
            )
            return meal_plan

    def test_filter_food_item_contents(cls):
        # Data shall be filtered from employee's meal plan data info
        food_item = cls._create_food_item_2(cls.employer)
        food_item.save()
        meal_plan = cls._create_meal_plan(cls.employee)
        meal_plan.save()
        cls.assertEqual(2, len(FoodItem.objects.all()))
        cuisine_text = meal_plan.cuisine
        dietary_restrictions_text = meal_plan.dietary_restrictions
        allergy_text = meal_plan.allergy
        filter_cuisine = re.sub(r'[^\w\s-]+', '', cuisine_text.lower())
        filter_dietary_restrictions = re.sub(r'[^\w\s-]+', '', dietary_restrictions_text.lower())
        filter_allergy = re.sub(r'[^\w\s-]+', '', allergy_text.lower())
        calories = meal_plan.calories
        price = meal_plan.budget
        food_item_filter = FoodItem.objects.filter(Q(price__lte=price)|Q(price__isnull=True),
                                cuisine_type__in=filter_cuisine.split(),
                                dietary_restrictions__in=filter_dietary_restrictions.split(),
                                calories__lte=calories,
                                ).exclude(allergy__in=filter_allergy.split())
        cls.assertEqual(2, len(food_item_filter))
        select_food_item = food_item_filter.get(food_name='Smoked Salmon', pk=1)
        cls.assertEqual('Smoked Salmon', select_food_item.food_name)
        cls.order = Order(employee=cls.employee)
        cls.order.save()
        cls.order.food_items.add(select_food_item)
        cls.assertEqual(1, len(cls.order.food_items.all()))

    @classmethod
    def tearDownClass(cls):
        ''' Invokes teardownClass method from test_base.py file of all
        test suites of the workrecords app for remoodwork. '''
        super().tearDownClass()

