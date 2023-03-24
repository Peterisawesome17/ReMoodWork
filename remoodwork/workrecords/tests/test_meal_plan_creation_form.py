from workrecords.tests.test_base import WorkRecordsTestCaseCounter
from workrecords.models import MealPlan
from workrecords.forms import MealAssessementCreationForm
from users.models import User, Employee


class MealAssessementCreationFormTestCase(WorkRecordsTestCaseCounter):
    @classmethod
    def setUpClass(cls):
        ''' Sets up test of a valid and invalid data inputs for meal plan
        assessement survey creation form '''
        cls.user = cls._create_an_employee()
        cls.employee = Employee.objects.create(user=cls.user)
        correct_meal_plan_form = {
            "calories": '300',
            "dietary_restrictions": "gluten-free",
            "goal": "To lose weight by 30 lbs",
            "allergy": "wheat",
            "budget": "20.00",
            "cuisine": "American"
        }
        cls.correct_meal_plan_form = MealAssessementCreationForm(data=correct_meal_plan_form)

    def test_meal_plan_form(cls):
        cls.assertTrue(cls.correct_meal_plan_form.is_valid())

    @classmethod
    def _create_an_employee(cls):
        ''' Sets up an employee creation used for creating and evaluating test
        cases for pulse survey '''
        username = 'adamsmart'
        password = 'anothertest666!'
        full_name = 'Adam Smart'
        email = 'adamsmart@test.com'
        company_name = 'Apple'
        job_classification_choice = 'EMPLOYEE'
        user = User(
            username=username,
            password=password,
            full_name=full_name,
            email=email,
            company_name=company_name,
            job_classification_choice=job_classification_choice
        )
        user.save()
        return user
