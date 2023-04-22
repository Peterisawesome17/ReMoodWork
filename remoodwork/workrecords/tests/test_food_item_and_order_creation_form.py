from workrecords.tests.test_base import WorkRecordsTestCaseCounter
from workrecords.forms import FoodItemCreationForm
from workrecords.models import FoodItem
from users.models import User, Employee, Employer


class FoodItemandOrderCreationFormTestCase(WorkRecordsTestCaseCounter):
    @classmethod
    def setUpClass(cls):
        super(WorkRecordsTestCaseCounter, cls).setUpClass()
        cls.employer = cls._create_an_employer()
        cls.employer.save()
        correct_food_item_restaurant_data_form = {
            'food_name': 'Smoked salmon',
            'description': 'Cooked and marinated with lemon juice',
            'price': 20.00,
            'cuisine_type': 'american',
            'food_item_type': 'restaurant',
            'restaurant_name': 'Dr.Dock\'s Seafood Restaurant',
            'calories': 200,
            'dietary_restrictions': 'gluten-free',
            'allergy': 'shellfish'
        }
        cls.correct_food_item_restaurant_form = FoodItemCreationForm(data=correct_food_item_restaurant_data_form)

    def test_valid_food_item_restaurant_form(cls):
        ''' Test 1: A valid test case to make sure the correct food item creation form
        is valid based on a restaurant food type item before saving its data content
        associated to food item model '''
        cls.assertTrue(cls.correct_food_item_restaurant_form.is_valid())

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
        cls.assertEqual(cls.correct_food_item_restaurant_form.data.get('food_name'),
                        food_item.food_name)
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



