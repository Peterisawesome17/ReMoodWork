from workrecords.forms import PulseSurveyCreationForm
from workrecords.models import PulseSurvey
from workrecords.tests.test_base import WorkRecordsTestCaseCounter
from users.models import User, Employee
from datetime import date

class PulseSurveyCreationFormTestCase(WorkRecordsTestCaseCounter):
    @classmethod
    def setUpClass(cls):
        ''' Sets up test cases of a valid and invalid data inputs
        for the pulse survey creation form shown in create_pulse_survey_page.html '''
        cls.user = cls._create_an_employee()
        cls.employee = Employee.objects.create(user=cls.user)
        correct_pulse_survey_data_form = {
            'activity_name': 'Created specifications report for campaign pages for an ecommerce',
            'activity_type': 'WT',
            'num_hours': '10',
            'emotional_rate_status': 'sleeping',
            'activity_description': 'Wrote two descriptive features deliveres for campaign pages ' \
                                    'of an ecommerce',
            'work_stressor_status': 'YES',
            'activity_created': date.today(),
            'employee_id': cls.employee.pk
        }
        cls.correct_pulse_survey_form = PulseSurveyCreationForm(data=correct_pulse_survey_data_form)

    def test_valid_pulse_survey_form(cls):
        ''' Test 1: A valid test case
        to make sure the correct pulse survey creation form is valid before
        saving its data content associated to pulse survey model'''
        cls.assertTrue(cls.correct_pulse_survey_form.is_valid())

    def test_created_pulse_survey(cls):
        ''' Test 2: A valid test case
        to see if a correct pulse survey creation form is saved
        for creating a new pulse survey record stored in
        a database model '''
        pass

    @classmethod
    def _create_an_employee(cls):
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