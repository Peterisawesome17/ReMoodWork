from workrecords.tests.test_base import WorkRecordsTestCaseCounter
from workrecords.models import MealPlan
from workrecords.forms import MealAssessementCreationForm
from users.models import User, Employee


class MealAssessementCreationFormTestCase(WorkRecordsTestCaseCounter):
    @classmethod
    def setUpClass(cls):
        ''' Sets up test of a valid and invalid data inputs for meal plan
        assessement survey creation form '''
        cls.user = cls._create_an_user()
        cls.employee = Employee.objects.create(user=cls.user)
        correct_meal_plan_form = {
            "calories": 300,
            "dietary_restrictions": "gluten-free",
            "goal": "To lose weight by 30 lbs",
            "allergy": "wheat",
            "budget": 20.00,
            "cuisine": "American"
        }
        cls.correct_meal_plan_form = MealAssessementCreationForm(data=correct_meal_plan_form)
        text_required_data_form = {
            "allergy": "peanuts",
            "cuisine": "Asian"
        }
        cls.text_required_form = MealAssessementCreationForm(data=text_required_data_form)

    def test_meal_plan_form_creation(cls):
        cls.assertTrue(cls.correct_meal_plan_form.is_valid())
        meal_plan = cls.correct_meal_plan_form.save(commit=False)
        meal_plan.employee = cls.employee
        cls.correct_meal_plan_form.save()
        cls.assertEqual(1, len(MealPlan.objects.all()))
        cls.assertEqual(meal_plan.employee, cls.correct_meal_plan_form.instance.employee)
        cls.assertEqual(cls.employee, cls.correct_meal_plan_form.instance.employee)
        cls.assertEqual(meal_plan.calories, cls.correct_meal_plan_form.data.get('calories'))
        cls.assertEqual(meal_plan.dietary_restrictions, cls.correct_meal_plan_form.data.get(
            'dietary_restrictions'
        ))
        cls.assertEqual(meal_plan.goal, cls.correct_meal_plan_form.data.get('goal'))
        cls.assertEqual(meal_plan.allergy, cls.correct_meal_plan_form.data.get('allergy'))
        cls.assertEqual(meal_plan.budget, cls.correct_meal_plan_form.data.get('budget'))
        cls.assertEqual(meal_plan.cuisine, cls.correct_meal_plan_form.data.get('cuisine'))

    def test_meal_plan_form_creation_update(cls):
        meal_plan = cls.correct_meal_plan_form.save(commit=False)
        meal_plan.employee = cls.employee
        cls.correct_meal_plan_form.save()
        cls.assertEqual(1, len(MealPlan.objects.all()))
        meal_plan_update = MealPlan.objects.get(employee=meal_plan.employee)
        incorrect_meal_plan_form = {
            "calories": -1,
            "dietary_restrictions": "gluten-free",
            "goal": "To lose weight by 30 lbs",
            "allergy": "wheat",
            "budget": 1.00,
            "cuisine": "American"
        }
        meal_plan_form = MealAssessementCreationForm(incorrect_meal_plan_form, instance=meal_plan_update)
        cls.assertFalse(meal_plan_form.is_valid())
        cls.assertEqual('Ensure this value is greater than or equal to 0.',
                        ''.join(meal_plan_form.errors.get('calories')))


    def test_required_invalid_text_form(cls):
        cls.assertFalse(cls.text_required_form.is_valid())
        required_field_text = 'This field is required.'
        cls.assertEqual(required_field_text,
                        ''.join(cls.text_required_form.errors.get('calories')))
        cls.assertEqual(required_field_text,
                        ''.join(cls.text_required_form.errors.get('dietary_restrictions')))
        cls.assertIsNone(cls.text_required_form.errors.get('goal'))
        cls.assertEqual(required_field_text,
                        ''.join(cls.text_required_form.errors.get('budget')))
