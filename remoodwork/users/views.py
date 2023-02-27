from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
# from django.contrib.auth.forms import UserCreationForm
from users.forms import UserRegistrationForm, UserLogInForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from users.models import Employee, Employer, User
from django.urls import reverse

# Create your views here.
def register_view(request):
    ''' Represents as a controller function for the user to register
    their information with their necessary credentials found from the model/forms
    of a user registration including their job classification status between an Employee and
    the Employer(later on) provided in remoodwork '''
    if request.method == 'POST':
        # If a user is requested to create and register their credential information
        form = UserRegistrationForm(request.POST)
        # Checks to see if a user registeration form can save its data content information
        # and store it into the User/Employee model of remoodwork's database table under
        # one condition (so far):
        # 1. If a username does not exists in the User/Employee model of remoodwork's database table
        # 2. If a full name of a User does not exists in the User/Employee model of remoodwork's
        # database table
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

def login_view(request):
    ''' Represents a controller function for the user(employee for now) to log in
    and authenticate their credentials using their username and password
    that redirects them to their home page of remoodwork '''
    context = {}
    if request.method == 'POST':
        form = UserLogInForm(data=request.POST)
        # Checks if a username and password are valid and verified first before redirecting users
        # To their home page site of remoodwork
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user:
                login(request=request, user=user)
                full_name = user.full_name
                messages.success(request=request, message=f'Welcome {full_name}!')
                return redirect('remoodwork-home')
        # Otherwise, if a user input their username and/or password credentials that are
        # invalid, then the user will be safely be redirected back to the log in page
        # to fufill their credntial information again
        else:
            context = {
                'form' : form
            }
    else:
        form = UserLogInForm()
        context = {
            'form' : form
        }
    return render(request=request, template_name='users/login_page.html', context=context)

def logout_view(request):
    ''' Represents a controller function for the user to log out of remoodwork
    from their exisiting credential '''
    logout(request=request)
    return render(request=request, template_name='users/logout_page.html')

def add_an_employee(request, pk, emp_pk):
    employee = get_object_or_404(Employee, user=emp_pk)
    employer = get_object_or_404(Employer, user=pk)
    employer_exists = Employer.objects.filter(pk=employer.pk)
    if request.method == 'POST':
        add_employee = request.POST.get('add_employee')
        if add_employee == 'yes':
            employer.employees.add(employee)
            url = reverse('remoodwork-pulse-survey', kwargs={'pk':emp_pk, 'emp_pk':pk})
            return redirect(url)
        elif add_employee == 'no':
            return redirect('remoodwork-home')
    else:
        return render(request=request, template_name='users/add_an_employee_page.html',
               context={'pk': pk, 'emp_pk': emp_pk, 'employer_exists': employer_exists})