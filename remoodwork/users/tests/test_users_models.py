from users.models import User, Employee, Employer
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
        cls.user2 = cls._create_new_user()
        cls.user2.save()


    def test_creating_user_info(cls):
        ''' Test 1: A valid test case that covers all the valid data attribute contents
        after creating a user model in remoodwork '''
        cls.assertNotEqual(0, len(User.objects.all()))
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
        cls.assertEqual(cls.job_classification_choice, cls.user1.job_classification_choice)
        # Tests a job classification status that exists in its choice used for User (employee)
        assert cls.user1.job_classification_choice in dict(User.CLASSIFICATION_CHOICE), \
            f'{cls.user1.job_classification_choice} not in a job classification status of a User'
        userslst = User.objects.get(pk=cls.user1.pk)
        dummy_user = userslst
        cls.assertEqual(dummy_user, cls.user1)

    def test_creating_employee(cls):
        ''' Test 2: A valid test case
        to see if an employee can be created after a user registers
        their account used in remoodwork. '''
        cls.assertEqual(0, len(Employee.objects.all()))
        if cls.user1.job_classification_choice == "EMPLOYEE":
            create_user = User.objects.get(username=cls.user1.username)
            dummy_employee, created = Employee.objects.get_or_create(user=create_user)
            cls.assertEqual(1, len(Employee.objects.all()))
            cls.assertTrue(created)
            cls.assertEqual(create_user, dummy_employee.user)
            # The only invalid test case in the overall content of this valid test case,
            # the same employee info should not be created again
            dummy_employee, created = Employee.objects.get_or_create(user=create_user)
            cls.assertFalse(created)
            cls.assertEqual(create_user, dummy_employee.user)

    def test_creating_employer(cls):
        ''' Test 3: A valid test case
        to see if an employer can be created after a user registers
        their account used in remoodwork '''
        cls.assertEqual(0, len(Employer.objects.all()))
        if cls.user2.job_classification_choice == 'EMPLOYER':
            create_user = User.objects.get(username=cls.user2.username)
            dummy_employer, created = Employer.objects.get_or_create(user=create_user)
            cls.assertEqual(1, len(Employer.objects.all()))
            cls.assertTrue(created)
            cls.assertEqual(create_user, dummy_employer.user)
            cls.assertEqual(0, len(dummy_employer.employees.all()))
            new_employee = Employee(user=cls.user1)
            new_employee.save()
            if new_employee.user.company_name == 'Google':
                dummy_employer.employees.add(new_employee)
            cls.assertNotEqual(0, len(dummy_employer.employees.all()))

    @classmethod
    def _create_new_user(cls):
        username = 'edwardsilverman'
        password = 'testing123!'
        full_name = 'Edward Silverman'
        email = 'esilverman@gmail.com'
        company_name = 'Google'
        job_classification_choice = 'EMPLOYER'
        user = User(
            username=username,
            password=password,
            full_name=full_name,
            email=email,
            company_name=company_name,
            job_classification_choice=job_classification_choice
        )
        return user


    @classmethod
    def tearDownClass(cls):
        ''' Invokes teardownClass method from test_base.py file of all
        test suites of the user app for remoodwork. '''
        super().tearDownClass()


