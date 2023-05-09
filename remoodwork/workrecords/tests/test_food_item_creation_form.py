from workrecords.tests.test_base import WorkRecordsTestCaseCounter
from workrecords.forms import FoodItemCreationForm
from workrecords.models import FoodItem
from users.models import User, Employee, Employer
from django.core.files.uploadedfile import SimpleUploadedFile
from remoodwork.settings import BASE_DIR
import os

class FoodItemandOrderCreationFormTestCase(WorkRecordsTestCaseCounter):
    @classmethod
    def setUpClass(cls):
        ''' Sets up test cases on testing creation form of food items created
        by employers '''
        super(WorkRecordsTestCaseCounter, cls).setUpClass()
        cls.employer = cls._create_an_employer()
        cls.employer.save()
        example_file = os.path.join(BASE_DIR,
                                    'workrecords/tests/food_meal_images_test', 'Example_Salmon.jpg')
        with open(example_file, 'rb') as file:
            example_file_image = file.read()
        food_meal_image = SimpleUploadedFile(
            name=os.path.basename(example_file),
            content=example_file_image,
            content_type="image/jpeg"
        )
        correct_food_item_restaurant_data_form = {
            'food_name': 'Smoked salmon',
            'description': 'Cooked and marinated with lemon juice',
            'price': 20.00,
            'cuisine_type': 'american',
            'food_item_type': 'restaurant',
            'restaurant_name': 'Dr.Dock\'s Seafood Restaurant',
            'calories': 200,
            'dietary_restrictions': 'gluten-free',
            'allergy': 'shellfish',
            'food_meal_image': food_meal_image
        }
        cls.correct_food_item_restaurant_form = FoodItemCreationForm(data=correct_food_item_restaurant_data_form,
                                                                     files=correct_food_item_restaurant_data_form)

        correct_food_item_recipe_data_form = {
            'food_name': 'Carne Asada',
            'description': 'This recipe will be good if you are a meat lover',
            'cuisine_type': 'mexican',
            'food_item_type': 'recipe',
            'recipe_url': 'https://loseweightbyeating.com/carne-asada-recipe/',
            'calories': 250,
            'dietary_restrictions': 'gluten-free',
            'allergy': 'beef'
        }

        cls.correct_food_item_recipe_form = FoodItemCreationForm(data=correct_food_item_recipe_data_form,
                                                                 files={})

        text_required_data_form = {
            'food_name': 'Goulash',
            'description': 'You will enjoy this meal if you like meat and vegetables',
        }

        invalid_choices_data_form = {
            'food_name': 'Strawberry Crepes',
            'description': 'Can be served during breakfast, lunch, or dinner',
            'cuisine_type': 'french',
            'food_item_type': 'other',
            'calories': 150,
            'dietary_restictions': 'glutenfree',
            'allergy': 'strawberry'
        }

        negative_num_calorie_data_form = {
            'food_name': 'Smoked salmon',
            'description': 'Cooked and marinated with lemon juice',
            'price': 20.00,
            'cuisine_type': 'american',
            'food_item_type': 'restaurant',
            'restaurant_name': 'Dr.Dock\'s Seafood Restaurant',
            'calories': -1,
            'dietary_restrictions': 'gluten-free',
            'allergy': 'shellfish'
        }

        cls.text_required_form = FoodItemCreationForm(data=text_required_data_form,
                                                      files={})

        cls.invalid_choices_form = FoodItemCreationForm(data=invalid_choices_data_form,
                                                        files={})

        cls.negative_num_calorie_form = FoodItemCreationForm(data=negative_num_calorie_data_form,
                                                             files={})

    def test_an_employer(cls):
        ''' Test 1: Valid test case to see if an Employer object lists only one
        Employer used for this test case. '''
        cls.assertNotEqual(0, len(Employer.objects.all()))

    def test_created_food_item_as_restaurant(cls):
        ''' Test 2: A valid test case to see if a correct food item creation form
        is saved as a restaurant food type item for creating a new food item stored in a
        database model '''
        cls.assertTrue(cls.correct_food_item_restaurant_form.is_valid())
        food_item = cls.correct_food_item_restaurant_form.save(commit=True)
        food_item.employer = cls.employer
        cls.correct_food_item_restaurant_form.save()
        cls.assertEqual(1, len(FoodItem.objects.all()))
        cls.assertEqual(cls.correct_food_item_restaurant_form.instance.employer, food_item.employer)
        food_item = FoodItem.objects.first()
        cls.assertEqual(cls.correct_food_item_restaurant_form.data.get('food_name'), food_item.food_name)
        cls.assertEqual(cls.correct_food_item_restaurant_form.data.get('description'),
                        food_item.description)
        cls.assertEqual(cls.correct_food_item_restaurant_form.data.get('price'),
                        food_item.price)
        cls.assertEqual(cls.correct_food_item_restaurant_form.data.get('cuisine_type'),
                        food_item.cuisine_type)
        cls.assertEqual(cls.correct_food_item_restaurant_form.data.get('food_item_type'),
                        food_item.food_item_type)
        cls.assertIsNone(cls.correct_food_item_restaurant_form.data.get('recipe_url'))
        cls.assertEqual(cls.correct_food_item_restaurant_form.data.get('restaurant_name'),
                        food_item.restaurant_name)
        cls.assertEqual(cls.correct_food_item_restaurant_form.data.get('calories'),
                        food_item.calories)
        cls.assertEqual(cls.correct_food_item_restaurant_form.data.get('dietary_restrictions'),
                        food_item.dietary_restrictions)
        cls.assertEqual(cls.correct_food_item_restaurant_form.data.get('allergy'), food_item.allergy)

        #Test if the image successfully uploads from a food item creation form
        assert cls.correct_food_item_restaurant_form.data.get('food_meal_image').name.strip('.jpg') in \
               os.path.basename(food_item.food_meal_image.url), f'Image not uploaded'
        cls.assertTrue(food_item.food_meal_image.url.startswith('/media'))

        cls.assertEqual(cls.correct_food_item_restaurant_form.instance.employer, food_item.employer)
        cls.assertEqual(1, len(FoodItem.objects.filter(employer=cls.correct_food_item_restaurant_form.instance.employer)))

    def test_valid_food_item_recipe_form(cls):
        ''' Test 3: A valid test case to see if a correct food item creation form
        is saved as a recipe food type item for creating a new food item stored in a
        database model '''
        cls.assertTrue(cls.correct_food_item_recipe_form.is_valid())
        food_item = cls.correct_food_item_recipe_form.save(commit=True)
        food_item.employer = cls.employer
        cls.correct_food_item_recipe_form.save()
        cls.assertEqual(1, len(FoodItem.objects.all()))
        cls.assertEqual(cls.correct_food_item_recipe_form.instance.employer, food_item.employer)
        food_item = FoodItem.objects.first()
        cls.assertEqual(cls.correct_food_item_recipe_form.data.get('food_name'), food_item.food_name)
        cls.assertEqual(cls.correct_food_item_recipe_form.data.get('description'),
                        food_item.description)
        cls.assertIsNone(cls.correct_food_item_recipe_form.data.get('price'))
        cls.assertEqual(cls.correct_food_item_recipe_form.data.get('price'), food_item.price)
        cls.assertEqual(cls.correct_food_item_recipe_form.data.get('cuisine_type'), food_item.cuisine_type)
        cls.assertEqual(cls.correct_food_item_recipe_form.data.get('food_item_type'),
                        food_item.food_item_type)
        cls.assertEqual(cls.correct_food_item_recipe_form.data.get('recipe_url'), food_item.recipe_url)
        cls.assertIsNone(cls.correct_food_item_recipe_form.data.get('restaurant_name'))
        cls.assertEqual(cls.correct_food_item_recipe_form.data.get('restaurant_name'),
                        food_item.restaurant_name)
        cls.assertEqual(cls.correct_food_item_recipe_form.data.get('calories'), food_item.calories)
        cls.assertEqual(cls.correct_food_item_recipe_form.data.get('dietary_restrictions'),
                        food_item.dietary_restrictions)
        cls.assertEqual(cls.correct_food_item_recipe_form.data.get('allergy'),
                        food_item.allergy)

        cls.assertIsNone(cls.correct_food_item_recipe_form.data.get('food_meal_image'))
        cls.assertEqual(food_item.food_meal_image.url, '/media/default.jpg')

    def test_required_invalid_text_form(cls):
        ''' Test 4: An invalid test case to see if an invalid food item creation
        is unable to be valid and will not be saved into its data content associated to its model '''
        cls.assertFalse(cls.text_required_form.is_valid())
        required_field_text = 'This field is required.'
        cls.assertEqual(required_field_text,
                        ''.join(cls.text_required_form.errors.get('cuisine_type')))
        cls.assertEqual(required_field_text,
                        ''.join(cls.text_required_form.errors.get('food_item_type')))
        cls.assertEqual(required_field_text,
                        ''.join(cls.text_required_form.errors.get('calories')))
        cls.assertEqual(required_field_text,
                        ''.join(cls.text_required_form.errors.get('dietary_restrictions')))
        cls.assertEqual(required_field_text,
                        ''.join(cls.text_required_form.errors.get('allergy')))

    def test_invalid_choice_options(cls):
        ''' Test 5: An invalid test case to see if an invalid food item creation
        is unable to be valid and will not be saved due to some invalid choices to create food item '''
        cls.assertFalse(cls.invalid_choices_form.is_valid())
        with cls.assertRaises(Exception):
            cls.invalid_choices_form.save(commit=True)

    def test_negative_num_calorie(cls):
        ''' Test 6: An invalid test case to see if calories attribute does not accept
        any negative numbers when creating a new food item '''
        cls.assertFalse(cls.negative_num_calorie_form.is_valid())
        valid_val_text = 'Ensure this value is greater than or equal to 0.'
        cls.assertEqual(valid_val_text,
                        ''.join(cls.negative_num_calorie_form.errors.get('calories')))