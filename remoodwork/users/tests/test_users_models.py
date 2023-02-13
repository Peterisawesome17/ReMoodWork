from users.models import User, Employee
from users.tests.test_base import UserTestCaseCounter


# Create your tests here.
class UserModelTestCases(UserTestCaseCounter):
    @classmethod
    def setUpClass(cls):
        ''' Sets up test cases of creating a new User model and
        fetching its provided data of the User. '''
        super(UserModelTestCases, cls).setUpClass()
        cls.username = 'johnsmith'
        cls.password = 'test123!'
        cls.full_name = 'John Smith'
        cls.email = 'johntsmith@gmail.com'
        cls.company_name = 'Google'
        cls.job_classification_choice = 'EMPLOYEE'
        cls.user1 = User(
            username=cls.username,
            password=cls.password,
            full_name=cls.full_name,
            email=cls.email,
            company_name=cls.company_name,
            job_classification_choice=cls.job_classification_choice
        )
        cls.user1.save()

    def test_all_user_model(cls):
        ''' Valid Test Case 1: Tests all the user models
        created in the remoodwork/default database tables'''
        cls.assertEqual(1, len(User.objects.all()))
        cls.countNum()

    def test_user_content_info(cls):
        ''' Valid Test Case 2: Tests all the valid data attribute contents
        after creating a user model in remoodwork '''
        # Tests an existing username that has recently been created
        cls.assertEqual(cls.username, cls.user1.username)
        # Tests an existing password that has recently been created
        cls.assertEqual(cls.password, cls.user1.password)
        # Tests an existing full name that has recently been created
        cls.assertEqual(cls.full_name, cls.user1.full_name)
        # Tests an existing email address name that has already been created
        cls.assertEqual(cls.email, cls.user1.email)
        # Tests an existing company name that has already been created
        cls.assertEqual(cls.company_name, cls.user1.company_name)
        # Tests a job classification status of a user that has already been created
        cls.assertEqual(cls.company_name, cls.user1.company_name)
        cls.countNum()

    def test_user_existence(cls):
        '''Tests to see if a new user is created in a user model of remoodwork system. '''
        userslst = User.objects.get(pk=cls.user1.pk)
        dummy_user = userslst
        cls.assertEqual(dummy_user, cls.user1)
        cls.countNum()

    def test_empty_employee(cls):
        ''' Checks to see  if there are no employees being created from a
        default database setup in remoodwork. '''
        cls.assertEqual(0, len(Employee.objects.all()))
        cls.countNum()

    def test_creating_employee(cls):
        ''' Checks to see if an employee can be created after a user registers
        their account used in remoodwork. '''
        employee1 = Employee(user=cls.user1)
        employee1.save()
        cls.assertEqual(1, len(Employee.objects.all()))
        dummy_user = User.objects.filter(username=cls.user1.username)[0]
        dummy_employee = Employee.objects.filter(pk=employee1.pk)[0]
        cls.assertEqual(dummy_user, dummy_employee.user)
        cls.countNum()

    def test_get_or_create_employee(cls):
        ''' Checks to see if an employee can be created or not
        after creating a user from a register page using
        get_or_create method used in User model. '''
        if cls.user1.job_classification_choice == "EMPLOYEE":
            create_user = User.objects.get(username=cls.user1.username)
            dummy_employee, created = Employee.objects.get_or_create(user=create_user)
            cls.assertTrue(created)
            cls.assertEqual(create_user, dummy_employee.user)
            dummy_employee, created = Employee.objects.get_or_create(user=create_user)
            cls.assertFalse(created)
            cls.assertEqual(create_user, dummy_employee.user)
        cls.countNum()


    @classmethod
    def tearDownClass(cls):
        ''' Used to display the total number of test cases passed with a complete percentage
                number for measuring a test suite of a user registration form test cases.
                It also displays the amount of failed test cases presented in the user registration
                form test cases. '''
        test_methods = set(test_method for test_method in cls.__dict__ if 'test' in test_method)
        tot_num_test_methods = len(test_methods)
        print(f'Ran {tot_num_test_methods} number of test cases in '
              f'{(cls.getNumOfTestCases()/tot_num_test_methods) * 100}% test suite of {cls.__name__}')
        num_of_failed_test_cases = tot_num_test_methods-cls.getNumOfTestCases()
        if num_of_failed_test_cases:
            print(f'Number of failed test cases occuring {num_of_failed_test_cases}')


