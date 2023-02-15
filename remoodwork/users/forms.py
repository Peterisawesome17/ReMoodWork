from django import forms
from users.models import User, Employee
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
class UserRegistrationForm(UserCreationForm, forms.ModelForm):
    ''' Used for producing a registration form for the user
    presented in a html register template page '''
    # password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'full_name', 'email', 'company_name', 'job_classification_choice']

    def save(self, commit=True):
        # Returns a model instance of the user without saving its model
        # used in a database table of remoodwork
        instance = super().save(commit=False)
        # Must provide a custom implementation logic of creating a user and an employee
        # (More will be touched upon later in this project)
        # if commit is evaluated true, then the model of a User/Employee will be
        # created in a database table of remoodwork
        if commit:
            instance.set_password(self.cleaned_data['password1'])
            # Save the user model in a database table of remoodwork
            instance.save()
            # Fetch user instance found from a user model of remoodwork database
            user_created = User.objects.get(username=instance.username)
            # Creates an Employee object instance model of a user
            # if user's job classification is an 'EMPLOYEE'
            if user_created.job_classification_choice == 'EMPLOYEE':
                employee, created = Employee.objects.get_or_create(user=user_created)
                # print(f'{employee} is created {created}')
        return instance

    def is_valid(self):
        is_valid = super().is_valid()
        if is_valid:
            # This is where the implementation of checking if a full name of the user
            # exists through a database table of remoodwork
            # Verify to see if a full name of the user already exists
            full_name_verify = self.cleaned_data.get('full_name')
            user_check = User.objects.filter(full_name=full_name_verify)
            if user_check.exists():
                self.add_error('full_name', 'A user with that full name already exists.')
                is_valid = False
        return is_valid

class UserLogInForm(AuthenticationForm):
    ''' Used for producing a login form for the user
    presented in a html login template page '''
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'password']
    # No need to override save and is_valid method for user login form class