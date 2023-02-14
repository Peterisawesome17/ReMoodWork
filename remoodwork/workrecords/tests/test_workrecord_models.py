from users.models import User, Employee
from workrecords.models import PulseSurvey
from workrecords.tests.test_base import WorkRecordsTestCaseCounter

class WorkRecordsTestCases(WorkRecordsTestCaseCounter):
    @classmethod
    def setUpClass(cls):
        ''' Sets up test cases for creating a pulse survey record of an employee model,
        where an employee shall be allowed to create one or more pulse survey records
        on remoodwork website. '''
        super(WorkRecordsTestCases, cls).setUpClass()
        cls.employee = cls._create_an_employee()
        cls.employee.save()

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

    def test_one_employee(cls):
        cls.assertEqual(1, len(Employee.objects.all()))
        # cls.countNum()

    def test_something(cls):
        cls.assertFalse(False)

    @classmethod
    def tearDownClass(cls):
        ''' Invokes teardownClass method from test_base.py file of all
        test suites of the workrecords app for remoodwork. '''
        super().tearDownClass()
