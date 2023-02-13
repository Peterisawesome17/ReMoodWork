from django.test import TestCase
from django.core.management import call_command

class UserTestCaseCounter(TestCase):
    ''' A test case basis to count all the passed test cases used to 
    test users app for remoodwork '''
    @classmethod
    def setUpClass(cls):
        ''' Initializes a set-up to count a number of test cases passed'''
        super(UserTestCaseCounter, cls).setUpClass()
        cls.count = 0

    @classmethod
    def countNum(cls):
        ''' Helper and mutator method to keep counting the number of test cases that were passed
        for each test suite script files made for the users app of remoodwork '''
        cls.count += 1

    @classmethod
    def getNumOfTestCases(cls):
        ''' Helper and a getter method to count a total number of test cases that were passed for
        each test suite script files made for the users app of remoodwork '''
        return cls.count
    
    @classmethod
    def tearDownClass(cls):
        ''' Used to display the total number of test cases passed with a complete percentage
        number for measuring each test suite of the user app for remoodwork.
        It also displays the amount of failed test cases presented in all test cases
        covered for each test suite of the user app for remoodwork. '''
        call_command('flush', interactive=False)
        test_methods = set(test_method for test_method in cls.__dict__ if 'test' in test_method)
        tot_num_test_methods = len(test_methods)
        print(f'Ran {tot_num_test_methods} number of test cases in '
              f'{(cls.getNumOfTestCases() / tot_num_test_methods) * 100}% test suite of {cls.__name__}')
        num_of_failed_test_cases = tot_num_test_methods - cls.getNumOfTestCases()
        if num_of_failed_test_cases:
            print(f'Number of failed test cases occuring {num_of_failed_test_cases}')
