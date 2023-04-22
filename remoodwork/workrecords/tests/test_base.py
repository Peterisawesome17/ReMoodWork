from django.test import TestCase
from django.core.management import call_command
from users.models import User, Employee, Employer

class WorkRecordsTestCaseCounter(TestCase):
    ''' A test case basis to count all the passed test cases used to
    test workrecords app for remoodwork '''

    countPreviousTestSuite = 0
    @classmethod
    def setUpClass(cls):
        ''' Initializes a set-up to count a number of test cases passed'''
        super(WorkRecordsTestCaseCounter, cls).setUpClass()
        cls.count = 0
        cls.test_result = None

    @classmethod
    def tearDownClass(cls):
        ''' Used to display the total number of test cases passed with a complete percentage
        number for measuring each test suite of the workrecords app for remoodwork.
        It also displays the amount of failed test cases or errors presented in all test cases
        covered for each test suite of the workrecords app for remoodwork. '''
        call_command('flush', interactive=False)
        result = cls.getResults()
        tot_test_cases = result.testsRun - WorkRecordsTestCaseCounter.countPreviousTestSuite
        WorkRecordsTestCaseCounter.countPreviousTestSuite = result.testsRun
        any_failure_tests = dict(result.failures)
        get_curr_test_suites = {testSuite.__class__.__name__ for testSuite in any_failure_tests.keys()}
        num_failed_test_cases = 0 if cls.__name__ not in get_curr_test_suites else len(result.failures)
        passed_test_cases = tot_test_cases - len(result.errors) - num_failed_test_cases
        print(f'Ran {tot_test_cases} number of test cases in '
              f'{(passed_test_cases / tot_test_cases) * 100}% test suite of '
              f'{cls.__name__}')
        if num_failed_test_cases:
            print(f'Total number of failed test cases: {len(result.failures)}')
        if result.errors:
            print(f'Number of errors in this test script: {len(result.errors)}')


    @classmethod
    def setResults(cls, result):
        ''' Helper and mutator method to get the number of test cases
        for each test suite script files made for the workrecords app of remoodwork '''
        cls.test_result = result

    @classmethod
    def getResults(cls):
        ''' Helper and a getter method to get a number of test cases
        for each test suite script files made for the workrecords app of remoodwork '''
        return cls.test_result

    @classmethod
    def _create_an_employee(cls):
        ''' Sets up an employee creation used for creating and evaluating test
        cases for pulse survey '''
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
    def _create_an_user(cls):
        ''' Sets up an employee creation used for creating and evaluating test
        cases for pulse survey '''
        username = 'adamsmart'
        password = 'anothertest666!'
        full_name = 'Adam Smart'
        email = 'adamsmart@test.com'
        company_name = 'Apple'
        job_classification_choice = 'EMPLOYEE'
        user = User.objects.create_user(
            username=username,
            password=password,
            full_name=full_name,
            email=email,
            company_name=company_name,
            job_classification_choice=job_classification_choice
        )
        return user

    @classmethod
    def _create_an_employer(cls):
        ''' Sets up an employer creation used for creating and evaluating test
        cases for creating food item '''
        username = 'tobeysmith'
        password = 'testingemployer123!'
        full_name = 'Tobey Smith'
        email = 'tobeysmith@test.com'
        company_name = 'Amazon'
        job_classification_choice = 'EMPLOYER'
        user = User(
            username=username,
            password=password,
            full_name=full_name,
            email=email,
            company_name=company_name,
            job_classification_choice=job_classification_choice
        )
        user.save()
        employer = Employer(user=user)
        return employer

    def run(self, result=None):
        super().run(result)
        self.setResults(result)


# Alternative to teardownClass if needed
#     ''' Used to display the total number of test cases passed with a complete percentage
#     number for measuring each test suite of the workrecords app for remoodwork.
#     It also displays the amount of failed test cases presented in all test cases
#     covered for each test suite of the workrecords app for remoodwork. '''
#     test_methods = set(test_method for test_method in cls.__dict__ if 'test' in test_method)
#     tot_num_test_methods = len(test_methods)
#     print(f'Ran {tot_num_test_methods} number of test cases in '
#           f'{(cls.getNumOfTestCases() / tot_num_test_methods) * 100}% test suite of {cls.__name__}')
#     num_of_failed_test_cases = tot_num_test_methods - cls.getNumOfTestCases()
#     if num_of_failed_test_cases:
#         print(f'Number of failed test cases occuring {num_of_failed_test_cases}')
# Alternative to teardownClass if needed

# Alternative if needed
# @classmethod
# def countNum(cls):
#     ''' Helper and mutator method to keep counting the number of test cases that were passed
#     for each test suite script files made for the workrecords app of remoodwork '''
#     cls.count += 1
#
# @classmethod
# def getNumOfTestCases(cls):
#     ''' Helper and a getter method to count a total number of test cases that were passed for
#     each test suite script files made for the workrecords app of remoodwork '''
#     return cls.count
#
# Alternative if needed
