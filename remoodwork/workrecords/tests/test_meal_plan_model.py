from users.models import User, Employee
from workrecords.tests.test_base import WorkRecordsTestCaseCounter
from workrecords.models import MealPlan

class MealPlanTestCase(WorkRecordsTestCaseCounter):
    @classmethod
    def setUpClass(cls):
        ''' Sets up test cases for creating a meal plan survey made for an employee
        where an employee shall be allowed to create a single one-to-one relationship
        of their meal plan assessment survey '''
        cls.employee = cls._create_an_employee()
        cls.employee.save()

    @classmethod
    def _create_meal_plan(cls, employee=None):
        ''' Create meal plan for test 2 '''
        meal_plan = None
        if employee:
            cls.calories = 190
            cls.dietary_restrictions = 'gluten-free'
            cls.goal = 'To lose weight by 30 lbs'
            cls.allergy = 'wheat'
            cls.budget = 20.00
            cls.cuisine = 'American'
            meal_plan = MealPlan(
                calories=cls.calories,
                dietary_restrictions=cls.dietary_restrictions,
                goal=cls.goal,
                allergy=cls.allergy,
                budget=cls.budget,
                cuisine=cls.cuisine,
                employee=cls.employee
            )
            return meal_plan

    def _create_another_meal_plan(cls, employee=None):
        ''' Create another meal plan for test 3 '''
        meal_plan = None
        if employee:
            cls.calories = 220
            cls.dietary_restrictions = 'vegetarian'
            cls.goal = 'To lose weight by 10 lbs'
            cls.allergy = 'meat'
            cls.budget = 30.00
            cls.cuisine = 'Greek'
            meal_plan = MealPlan(
                calories=cls.calories,
                dietary_restrictions=cls.dietary_restrictions,
                goal=cls.goal,
                allergy=cls.allergy,
                budget=cls.budget,
                cuisine=cls.cuisine,
                employee=cls.employee
            )
            return meal_plan

    def test_one_employee(cls):
        ''' Test 1: Valid test case to see if an Employee object lists only one
        Employee used for this test case. '''
        cls.assertEqual(1, len(Employee.objects.all()))

    def test_meal_plan(cls):
        ''' Test 2: Valid test case to see if a meal plan has already been created
        and provides its contents made after creating a meal plan made by an employee '''
        meal_plan = cls._create_meal_plan(cls.employee)
        meal_plan.save()
        cls.assertEqual(1, len(MealPlan.objects.all()))
        # Checks all contents of meal plan
        cls.assertEqual(cls.calories, meal_plan.calories)
        cls.assertEqual(cls.dietary_restrictions, meal_plan.dietary_restrictions)
        cls.assertEqual(cls.goal, meal_plan.goal)
        cls.assertEqual(cls.allergy, meal_plan.allergy)
        cls.assertEqual(cls.budget, meal_plan.budget)
        cls.assertEqual(cls.cuisine, meal_plan.cuisine)
        cls.assertEqual(cls.employee, meal_plan.employee)

    def test_no_dup_meal_plan(cls):
        ''' Test 3: Invalid test case to see if a meal plan can only be created once made
        by an employee (There cannot be more than one meal plan (a one-to-one relationship)) '''
        meal_plan = cls._create_meal_plan(cls.employee)
        meal_plan.save()
        with cls.assertRaises(Exception):
            meal_plan_dup = cls._create_another_meal_plan(cls.employee)
            meal_plan_dup.save()


    @classmethod
    def tearDownClass(cls):
        ''' Invokes tearDownClass method from test_base.py file of all
        test suites of the workrecords app for remoodwork '''
        super().tearDownClass()

