from django import forms
from users.models import User
class UserRegisterationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'first_name', 'last_name', 'email', 'company_name', 'job_classification_choice']
