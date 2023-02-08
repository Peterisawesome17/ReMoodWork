from django import forms
from users.models import User, Employee
class UserRegistrationForm(forms.ModelForm):
    ''' Used for producing a registration form for the user
    presented in an html register template page '''
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'password', 'full_name', 'email', 'company_name', 'job_classification_choice']

    # def save(self, commit=True):
    #     user_instance = super().save(commit=False)
    #     # Must provide a custom implementation logic of creating a user and an employee
    #     # (More will be touched upon later in this project)
    #     if commit:
    #         user_instance.save()
    #         # employee = Employee(user=)