from workrecords.forms import PulseSurveyCreationForm
from workrecords.models import PulseSurvey
from users.models import User, Employee, Employer
from workrecords.tests.test_base import WorkRecordsTestCaseCounter
from datetime import date

class PulseSurveyCreationFormTestCase(WorkRecordsTestCaseCounter):
    @classmethod
    def setUpClass(cls):
        ''' Sets up test cases of a valid and invalid data inputs
        for the pulse survey creation form shown in create_pulse_survey_page.html '''
        cls.employee = cls._create_an_employee()
        cls.employee.save()
        correct_pulse_survey_data_form = {
            'activity_name': 'Created specifications report for campaign pages for an ecommerce',
            'activity_type': 'WT',
            'num_hours': '10',
            'emotional_rate_status': 'sleeping',
            'activity_description': 'Wrote two descriptive features deliveres for campaign pages ' \
                                    'of an ecommerce',
            'work_stressor_status': 'YES',
            'activity_created': date.today(),
        }
        cls.correct_pulse_survey_form = PulseSurveyCreationForm(data=correct_pulse_survey_data_form)
        create_same_activity_name_data_form = {
            'activity_name': 'Created specifications report for campaign pages for an ecommerce',
            'activity_type': 'WT',
            'num_hours': '10',
            'emotional_rate_status': 'sleeping',
            'activity_description': 'Wrote two descriptive features deliveres for campaign pages ' \
                                    'of an ecommerce',
            'work_stressor_status': 'YES',
            'activity_created': date.today(),
        }
        cls.create_same_activity_name_form = PulseSurveyCreationForm(data=create_same_activity_name_data_form)
        text_required_data_form = {
            'activity_name': 'Office party',
            'num_of_hours': '3'
        }
        cls.text_required_form = PulseSurveyCreationForm(data=text_required_data_form)

    def test_one_employee(cls):
        ''' Test 1: Valid test case to see if an Employee object lists only one
        Employee used for this test case. '''
        cls.assertEqual(1, len(Employee.objects.all()))

    def test_created_pulse_survey(cls):
        ''' Test 2: A valid test case
        to see if a correct pulse survey creation form is saved
        for creating a new pulse survey record stored in
        a database model '''
        cls.assertTrue(cls.correct_pulse_survey_form.is_valid())
        pulse_survey = cls.correct_pulse_survey_form.save(commit=False)
        pulse_survey.employee = cls.employee
        cls.correct_pulse_survey_form.save()
        cls.assertEqual(1, len(PulseSurvey.objects.all()))
        cls.assertEqual(cls.correct_pulse_survey_form.instance.employee, pulse_survey.employee)
        cls.assertEqual(cls.employee, cls.correct_pulse_survey_form.instance.employee)
        pulse_survey_record = PulseSurvey.objects.first()
        cls.assertEqual(cls.correct_pulse_survey_form.data.get('activity_name'),
                        pulse_survey_record.activity_name)
        cls.assertEqual(cls.correct_pulse_survey_form.data.get('activity_type'),
                        pulse_survey_record.activity_type)
        cls.assertEqual(cls.correct_pulse_survey_form.data.get('num_hours'),
                        pulse_survey_record.num_hours)
        cls.assertEqual(cls.correct_pulse_survey_form.data.get('emotional_rate_status'),
                        pulse_survey_record.emotional_rate_status)
        cls.assertEqual(cls.correct_pulse_survey_form.data.get('activity_description'),
                        pulse_survey_record.activity_description)
        cls.assertEqual(cls.correct_pulse_survey_form.data.get('work_stressor_status'),
                        pulse_survey_record.work_stressor_status)
        cls.assertEqual(cls.correct_pulse_survey_form.data.get('activity_created'),
                        pulse_survey_record.activity_created)

    def test_activity_name_already_created(cls):
        ''' Test 3: An invalid test case to see if an activity name has already
        been created from one of the pulse surveys done by an employee '''
        pulse_survey = cls.correct_pulse_survey_form.save(commit=False)
        pulse_survey.employee = cls.employee
        cls.correct_pulse_survey_form.save()
        cls.assertEqual(1, len(PulseSurvey.objects.all()))
        # Should be invalid due an existing activity name created from one of the pulse
        # surveys done by an employee
        cls.assertFalse(cls.create_same_activity_name_form.is_valid())
        assert 'This activity name already exists from one of your pulse survey records.' in \
               cls.create_same_activity_name_form.errors.get('activity_name') , \
            'Should not create the same activity name as a new pulse survey record'

    def test_required_invalid_text_form(cls):
        ''' Test 4: An invalid test cases to see if an invalid
        pulse survey creation form is unable to be valid and will not be saved
        into its data content associated to its model'''
        cls.assertFalse(cls.text_required_form.is_valid())
        required_field_text = 'This field is required.'
        cls.assertEqual(required_field_text,
                        ''.join(cls.text_required_form.errors.get('activity_type')))
        cls.assertEqual(required_field_text,
                        ''.join(cls.text_required_form.errors.get('emotional_rate_status')))
        cls.assertIsNone(cls.text_required_form.errors.get('activity_description'))
        cls.assertEqual(required_field_text,
                        ''.join(cls.text_required_form.errors.get('work_stressor_status')))

    @classmethod
    def tearDownClass(cls):
        ''' Invokes teardownClass method from test_base.py file of all
        test suites of the user app for remoodwork. '''
        super().tearDownClass()