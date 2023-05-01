from users.models import Employer, Employee
from workrecords.tests.test_base import WorkRecordsTestCaseCounter
from workrecords.models import FoodItem, MealPlan, Order
from workrecords.views import filter_food_item

class OrderFoodItemTestCase(WorkRecordsTestCaseCounter):
    @classmethod
    def setUpClass(cls):
        ''' Sets up test cases for creating Order data model for ordering food meal items
        by an employee on remoodwork website '''
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

    @classmethod
    def _create_meal_plan(cls, employee=None):
        ''' Sets up a meal plan assessment to
        integrate and filter out a list of food meal items from an employee's info '''
        meal_plan = None
        if employee:
            cls.calories = 400
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

    @classmethod
    def _create_food_item_1(cls, employer):
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
    def _create_food_item_2(cls, employer):
        ''' Sets up the second food item to make some test cases
        on creating a food meal item indicated as a recipe. '''
        if employer:
            food_name = 'Texas-Style Beef Brisket'
            description = 'This recipe is the best if you love BBQ'
            cuisine_type = 'american'
            food_item_type = 'recipe'
            recipe_url = 'https://www.tasteofhome.com/recipes/texas-style-beef-brisket/'
            calories = 381
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

    def test_an_employee(cls):
        ''' Test 1: Valid test case to see if an Employee object lists only one
        Employee used for this test case. '''
        cls.assertEqual(1, len(Employee.objects.all()))
        employee = Employee.objects.get(user=cls.employee.user.pk)
        cls.assertEqual(cls.employee.user.full_name, employee.user.full_name)


    def test_an_employer(cls):
        ''' Test 2: Valid test case to see if an Employer object lists only one
        Employer used for this test case. '''
        cls.assertEqual(1, len(Employer.objects.all()))
        employer = Employer.objects.get(user=cls.employer.user.pk)
        cls.assertEqual(cls.employer.user.full_name, employer.user.full_name)

    def test_meal_plan(cls):
        ''' Test 3: Valid test case to see if a Meal Plan is created once
        by an Employee '''
        cls.assertEqual(1, len(Employer.objects.all()))
        meal_plan = MealPlan.objects.get(employee=cls.employee)
        cls.assertEqual(cls.meal_plan, meal_plan)

    def test_food_items(cls):
        ''' Test 4: Valid test to see if an Employer created two food meal items '''
        fooditems_employer = FoodItem.objects.filter(employer=cls.employer)
        cls.assertEqual(2, len(fooditems_employer))
        food_item_1 = fooditems_employer.get(food_name=cls.food_item.food_name)
        cls.assertEqual(cls.food_item.food_name, food_item_1.food_name)
        food_item_2 = fooditems_employer.get(food_name=cls.another_food_item.food_name)
        cls.assertEqual(cls.another_food_item.food_name, food_item_2.food_name)

    def test_filter_and_order_food_item(cls):
        ''' Test 5: Valid test to see if this system achieves an algorithm
        in filtering food items based on Employee's meal planning assessment info
        and verify to see if a food meal item can become ordered and placed
        in remoodwork's system. '''
        food_item_filter = filter_food_item(cls.meal_plan, cls.employee.user.company_name)
        cls.assertIsNotNone(food_item_filter)
        cls.assertEqual(2, len(food_item_filter))
        select_food_item = food_item_filter.get(food_name='Smoked Salmon', pk=1)
        cls.assertEqual("Smoked Salmon", select_food_item.food_name)
        cls.order = Order(employee=cls.employee)
        cls.order.save()
        cls.order.food_items.add(select_food_item)
        cls.assertEqual(1, len(cls.order.food_items.all()))
        cls.assertEqual(1, len(Order.objects.all()))
        order_created = Order.objects.get(pk=cls.order.pk)
        find_food_item = cls.order.food_items.get(food_name='Smoked Salmon')
        assert find_food_item in order_created.food_items.all(), 'Food item not found'

    @classmethod
    def tearDownClass(cls):
        ''' Invokes teardownClass method from test_base.py file of all
        test suites of the workrecords app for remoodwork. '''
        super().tearDownClass()