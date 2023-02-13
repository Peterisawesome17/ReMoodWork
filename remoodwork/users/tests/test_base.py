from django.test import TestCase

class UserTestCaseCounter(TestCase):
    @classmethod
    def setUpClass(cls):
        ''' Initializes a set up to count a number of test cases passed'''
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
