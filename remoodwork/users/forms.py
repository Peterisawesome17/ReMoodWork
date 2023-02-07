from django import forms
from users.models import User
class UserRegistrationForm(forms.ModelForm):
    ''' Used for producing a registration form for the user
    presented in an html register template page '''
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'password', 'first_name', 'last_name', 'email', 'company_name', 'job_classification_choice']
