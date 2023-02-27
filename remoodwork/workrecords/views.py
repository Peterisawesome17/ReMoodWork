from django.shortcuts import render, redirect
from django.http import HttpResponse # Used for testing http response to view web pages of remoodwork's workrecords - Peter
from datetime import datetime # Useful for implementing pulse survey page later in this project - Peter
from workrecords.forms import PulseSurveyCreationForm
from users.models import Employee, User, Employer
from django.contrib import messages
from workrecords.models import PulseSurvey
from django.contrib.auth.decorators import login_required, user_passes_test

# Create your views here.
# Used for creating a main website of remoodwork and work record logs of an employee- Peter
# Will also be used to create pulse surveys to employees - Peter


def home_view(request):
    '''A view of a home website page of remoodwork'''
    # Only displays a list of pulse survey records from the employee (user)
    # and will also be the main home page of remoodwork for adding few features later on
    pulse_survey_records, employees_with_same_company_name, employer_exists, employee_exists = [None]*4
    company_name_title = ''
    if request.user.id:
        curr_user = User.objects.get(pk=request.user.id)
        employer_exists, employee_exists = Employer.objects.filter(user=curr_user)\
            , Employee.objects.filter(user=curr_user)
        if employee_exists.exists():
            employee = Employee.objects.get(user=curr_user)
            pulse_survey_records = PulseSurvey.objects.filter(employee=employee)
        if employer_exists.exists():
            employer = Employer.objects.get(user=curr_user)
            employees_with_same_company_name = Employee.objects.filter(
                user__job_classification_choice = 'EMPLOYEE',
                user__company_name = curr_user.company_name
            )
            company_name_title =  curr_user.company_name
    context =  {
        'user_id': request.user.id,
        'employee_pulse_survey_records': pulse_survey_records,
        'employer_employee_list': employees_with_same_company_name,
        'employer_exists': employer_exists,
        'employee_exists': employee_exists,
        'company_name_title': company_name_title,
        'employer': employer
    }
    return render(request=request, template_name='workrecords/home_page.html', context=context)

def pulse_survey_view(request, pk):
    '''A view of a pulse survey page where employee creates their work/activity record logs'''
    # This controller function must include a list of survey records that were created
    # by and employee (user),
    # otherwise it will return a message to the employee
    # 'Hmm..it looks like to me that you have not created any recent pulse survey records'
    pulse_survey_record = None
    if pk:
        user = User.objects.get(pk=pk)
        employee = Employee.objects.get(user=user)
        pulse_survey_records = PulseSurvey.objects.filter(employee=employee)
        employer_exists, employee_exists = Employer.objects.filter(user=user) \
            , Employee.objects.filter(user=user)
    context = {
        'user_id': pk,
        'pulse_survey_records': pulse_survey_records,
        'employee_exists': employee_exists,
        'employer_exists': employer_exists
    }
    return render(request=request,
                  template_name='workrecords/pulse_survey_main_page.html',
                  context=context)

def create_pulse_survey_view(request, pk):
    ''' A view controller to create pulse surveys produced by an employee (user)'''
    user = User.objects.get(pk=pk)
    employee = Employee.objects.get(user=user)
    employee_exists = Employee.objects.filter(user=user)
    if request.method == 'POST':
        pulse_survey_form = PulseSurveyCreationForm(request.POST)
        if pulse_survey_form.is_valid():
            pulse_survey = pulse_survey_form.save(commit=False)
            pulse_survey.employee = employee
            pulse_survey_form.save()
            activity_name = pulse_survey_form.cleaned_data.get('activity_name')
            messages.success(request=request, message=f'{activity_name} successfully created '
                                                      f'from your pulse survey records')
            return redirect('remoodwork-pulse-survey', pk=pk)
        else:
            context = {
                'form': pulse_survey_form,
                'employee_exists': employee_exists
            }
    else:
        pulse_survey_form = PulseSurveyCreationForm()
        context = {
            'form': pulse_survey_form,
            'employee_exists': employee_exists
        }
    return render(request=request,
                  template_name='workrecords/create_pulse_survey_page.html',
                  context=context)
