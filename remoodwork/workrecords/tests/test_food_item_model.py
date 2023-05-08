from users.models import Employer
from workrecords.tests.test_base import WorkRecordsTestCaseCounter
from workrecords.models import FoodItem
from django.core.files.uploadedfile import SimpleUploadedFile
from remoodwork.settings import BASE_DIR
import os

class FoodItemandOrderTestCase(WorkRecordsTestCaseCounter):
    @classmethod
    def setUpClass(cls):
        ''' Sets up test cases for creating a food item made by an employer
        where it shall be allowed to create one or more food items on remoodwork website '''
        super(WorkRecordsTestCaseCounter, cls).setUpClass()
        cls.employer = cls._create_an_employer()
        cls.employer.save()

    @classmethod
    def _create_food_item_1(cls, employer):
        ''' Sets up the first food item to make some test cases
        on creating a food meal item indicated as a restaurant. '''
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
            example_file = os.path.join(BASE_DIR,
                                   'workrecords/tests/food_meal_images_test', 'Example_Steak.jpg')
            with open(example_file, 'rb') as file:
                example_file_image = file.read()
            food_meal_image = SimpleUploadedFile(
                name=os.path.basename(example_file),
                content=example_file_image,
                content_type="image/jpeg"
            )
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
                food_meal_image=food_meal_image,
                employer=employer
            )
            return food_item

    def _create_food_item_2(cls, employer):
        ''' Sets up the second food item to make some test cases
        on creating a food meal item indicated as a recipe. '''
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
        ''' Test 1: Valid test case to see if an Employer object lists only one
        Employer used for this test case. '''
        cls.assertNotEqual(0, len(Employer.objects.all()))

    def test_food_item_model_1(cls):
        ''' Test 2: Valid test to see if an employer creates a new food meal item
        from a given restaurant. '''
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

        #Test if an image uploads from food item model
        cls.assertEqual(food_item.food_meal_image.url, food_item_match.food_meal_image.url)

        cls.assertEqual(food_item.employer, food_item_match.employer)

    def test_food_item_model_2(cls):
        ''' Test 3: Valid test to see if an employer creates a new food meal item
        from a given recipe '''
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
        # Checks
        with cls.assertRaises(AssertionError):
            assert food_item.food_meal_image, 'Meal image not uploaded'
        cls.assertEqual(food_item.employer, food_item_match.employer)

    @classmethod
    def tearDownClass(cls):
        ''' Invokes teardownClass method from test_base.py file of all
        test suites of the workrecords app for remoodwork. '''
        super().tearDownClass()

