from django.shortcuts import render, HttpResponse, redirect
# from django.contrib.auth.forms import UserCreationForm
from users.forms import UserRegistrationForm
from django.contrib import messages

# Create your views here.
def register_view(request):
    '''Represents as a controller function for the user to register
    their information with their necessary credentials found from the model/forms
    of a user registration including their job classification staus between an Employee and
    the Employer provided in remoodwork'''
    if request.method == 'POST':
        # If a user is requested to create and register their credential information
        form = UserRegistrationForm(request.POST)
        # Checks to see if a user registeration form can save its data content information
        # and store it into the User/Employee model of remoodwork's database table under
        # one condition (so far):
        # 1. If a username does not exists in the User/Employee model of remoodowrk's database table
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request=request, message=f'Account created for {username}')
            return redirect('remoodwork-home')
        else:
            # Otherwise, if a username already exists in remoodwork's database table,
            # then the user will safely be redirected back to the register page to fufill
            # their credential information again
            context = {
                'form': form,
            }
            return render(request=request, template_name='users/register_page.html', context=context)
    else:
        form = UserRegistrationForm()
        context = {
        'form' : form,
        }
        return render(request=request, template_name='users/register_page.html', context=context)