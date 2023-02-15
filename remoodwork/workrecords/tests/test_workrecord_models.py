from users.models import User, Employee
from workrecords.models import PulseSurvey
from workrecords.tests.test_base import WorkRecordsTestCaseCounter
import emoji
from datetime import date

class WorkRecordsTestCases(WorkRecordsTestCaseCounter):
    @classmethod
    def setUpClass(cls):
        ''' Sets up test cases for creating a pulse survey record of an employee model,
        where an employee shall be allowed to create one or more pulse survey records
        on remoodwork website. '''
        super(WorkRecordsTestCases, cls).setUpClass()
        cls.employee = cls._create_an_employee()
        cls.employee.save()
        cls.pulsesurvey = cls._create_pulse_survey_1(cls.employee)
        cls.pulsesurvey.save()

    @classmethod
    def _create_an_employee(cls):
        username = 'mikerandy'
        password = 'anothertest555!'
        full_name = 'Mike Randy'
        email = 'mikerandy@test.com'
        company_name = 'Amazon'
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
        employee = Employee(user=user)
        return employee
    @classmethod
    def _create_pulse_survey_1(cls, employee=None):
        pulse_survey = None
        if employee:
            cls.activity_name = 'Implemented campaign feature test cases for ecommerce website'
            cls.activity_type = 'WT'
            cls.num_hours = '10'
            cls.emotional_rate_status = "taking_break_or_vacation"
            cls.activity_description = 'I have created 5 additional test cases of a campaign feature' \
                                   'used for ecommerce website'
            cls.work_stressor_status = 'NO'
            cls.activity_created = date.today()
            pulse_survey = PulseSurvey(
                activity_name=cls.activity_name,
                activity_type=cls.activity_type,
                num_hours=cls.num_hours,
                emotional_rate_status=cls.emotional_rate_status,
                activity_description=cls.activity_description,
                work_stressor_status=cls.work_stressor_status,
                activity_created=cls.activity_created,
                employee=employee
            )
        return pulse_survey

    def test_one_employee(cls):
        '''Test 1: Valid test case to see if an Employee object lists only one
        Employee used for this test case'''
        cls.assertEqual(1, len(Employee.objects.all()))
        # cls.countNum()

    def test_emoji_reactions(cls):
        '''Test 2: Valid test case to see all the valid emoji reactions
        tested for creating pulse survey records of workrecords in remoodwork '''
        emoji_reactions = dict(PulseSurvey.EMOJI_STATUS_CHOICE)
        for emoji_reaction in emoji_reactions.values():
            assert True == emoji.is_emoji(emoji_reaction), \
                f'{emoji_reaction} is not an emoji reaction'

    def test_pulse_survey_content(cls):
        '''Test 3: Valid test case to see the contents and data attributes
        of creating a pulse survey record of workrecords in remoodwork '''
        # Tests an existing activity name that has recently been created
        cls.assertEqual(cls.activity_name, cls.pulsesurvey.activity_name)
        # Tests an existing activity type that has recently been created
        cls.assertEqual(cls.activity_type, cls.pulsesurvey.activity_type)
        # Tests an activity type that exists in its choice used for PulseSurvey record
        assert cls.pulsesurvey.activity_type in dict(PulseSurvey.ACTIVITY_TYPE_CHOICES), \
            f'{cls.pulsesurvey.activity_type} not in Pulse Survey activity type choices'
        # Tests an existing number of hours spend on an activity that has recently been created
        cls.assertEqual(cls.num_hours, cls.pulsesurvey.num_hours)
        # Tests an emotional rate status of an activity (assuming that an employee already created)
        cls.assertEqual(cls.emotional_rate_status, cls.pulsesurvey.emotional_rate_status)
        # Tests an emotional rate status that exists in its choice used for PulseSurvey record
        assert cls.pulsesurvey.emotional_rate_status in dict(PulseSurvey.EMOJI_STATUS_CHOICE), \
            f'{cls.pulsesurvey.emotional_rate_status} not in Pulse Survey emotional status choices'
        # Tests an optional existing activity description that has recently been created
        cls.assertEqual(cls.activity_description, cls.pulsesurvey.activity_description)
        # Tests a work stressor status of an activity (assuming that an employee already created)
        cls.assertEqual(cls.work_stressor_status, cls.pulsesurvey.work_stressor_status)
        # Tests a work stressor status that exists in its choice used for PulseSurvey record
        assert cls.pulsesurvey.work_stressor_status in dict(PulseSurvey.WORK_STRESSOR_STATUS_CHOICE), \
            f'{cls.pulsesurvey.work_stressor_status} not in Pulse Survey work stressor choices'
        # Tests an existing activity created that has recently been created
        cls.assertEqual(cls.activity_created, cls.pulsesurvey.activity_created)
        # Tests if a pulse survey was recently created by the right employee
        cls.assertEqual(cls.employee, cls.pulsesurvey.employee)

    def test_all_pulse_survey(cls):
        '''Test 4: Valid test case to see if any pulse surveys
        have already created by the right employee'''
        cls.assertEqual(1, len(cls.employee.pulse_survey.all()))
        another_pulse_survey = cls._create_pulse_survey_2(cls.employee)
        another_pulse_survey.save()
        #Should have about 2 pulse surveys created by an employee
        cls.assertEqual(2, len(cls.employee.pulse_survey.all()))
        dummy_pulse_survey = PulseSurvey.objects.get(pk=cls.pulsesurvey.pk)
        cls.assertNotEqual(dummy_pulse_survey, another_pulse_survey)

    def test_only_one_pulse_survey(cls):
        '''Test 5: Valid test case to see if there is only
        one pulse survey already created by an employee for this test case'''
        cls.assertEqual(1, len(cls.employee.pulse_survey.all()))
    def _create_pulse_survey_2(cls, employee=None):
        pulse_survey = None
        if employee:
            cls.activity_name = 'Taco Party'
            cls.activity_type = 'TB'
            cls.num_hours = '1'
            cls.emotional_rate_status = "taking_break_or_vacation"
            cls.activity_description = 'Celebrating taco party with a few of my coworkers at a break room!'
            cls.work_stressor_status = 'NO'
            cls.activity_created = date.today()
            pulse_survey = PulseSurvey(
                activity_name=cls.activity_name,
                activity_type=cls.activity_type,
                num_hours=cls.num_hours,
                emotional_rate_status=cls.emotional_rate_status,
                activity_description=cls.activity_description,
                work_stressor_status=cls.work_stressor_status,
                activity_created=cls.activity_created,
                employee=employee
            )
        return pulse_survey

    @classmethod
    def tearDownClass(cls):
        ''' Invokes teardownClass method from test_base.py file of all
        test suites of the workrecords app for remoodwork. '''
        super().tearDownClass()
