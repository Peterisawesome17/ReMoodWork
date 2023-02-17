from django.shortcuts import render, redirect
from django.http import HttpResponse # Used for testing http response to view web pages of remoodwork's workrecords - Peter
from datetime import datetime # Useful for implementing pulse survey page later in this project - Peter
from workrecords.forms import PulseSurveyCreationForm
from users.models import Employee, User
from django.contrib import messages

# Create your views here.
# Used for creating a main website of remoodwork and work record logs of an employee- Peter
# Will also be used to create pulse surveys to employees - Peter

# Dummy data for how it will look like on the home page of remoodwork site - Peter
log_records = [
    {
        'title': 'Wrote five test cases to cover additional features of an app',
        'posted_date': '07/20/2023',
        'category_type': 'Work task',
        'number_of_hours': '5',
        'location': 'San Diego',
        'emoji_face': '\N{tired face}'
    },
    {
        'title': 'Riding a short walk',
        'posted_date': '08/13/2023',
        'category_type': 'Taking a break',
        'number_of_hours': '1',
        'location': 'San Diego',
        'emoji_face': '\N{grinning face}'
    },
    {
        'title': 'Taking a trip to Spain',
        'posted_date': datetime.today(),
        'category_type': 'Vacation Trip',
        'number_of_hours': '64',
        'location': 'San Diego',
        'emoji_face': '\N{smiling face with sunglasses}'
    }
]

def home_view(request):
    '''A view of a home website page of remoodwork'''
    # More details will be added later on
    # Default return to check an http reponse of a web page
    context =  {
        'log_records': log_records
    }
    return render(request=request, template_name='workrecords/home_page.html', context=context)

def pulse_survey_view(request):
    '''A view of a pulse survey page where employee creates their work/activity record logs'''
    #Update 1: Will be used to print out today's date of a work/activity record logs of an employee later on
    date_today = datetime.today()
    # {{date_today}} in the templates (later on) for context - Peter

    # This controller function must include a list of survey records that were created
    # by and employee (user),
    # otherwise it will return a message to the employee
    # 'Hmm..it looks like to me that you have not created any recent pulse survey records'
    context = {
        'user_id': request.user.id
    }
    return render(request=request,
                  template_name='workrecords/pulse_survey_main_page.html',
                  context=context)

def create_pulse_survey_view(request, pk):
    user = User.objects.get(pk=pk)
    employee = Employee.objects.get(user=user)
    if request.method == 'POST':
        pulse_survey_form = PulseSurveyCreationForm(request.POST)
        if pulse_survey_form.is_valid():
            pulse_survey = pulse_survey_form.save(commit=False)
            pulse_survey.employee = employee
            pulse_survey_form.save()
            activity_name = pulse_survey_form.cleaned_data.get('activity_name')
            messages.success(request=request, message=f'{activity_name} successfully created '
                                                      f'from your pulse survey records')
            return redirect('remoodwork-pulse-survey')
        else:
            context = {
                'form': pulse_survey_form
            }
    else:
        pulse_survey_form = PulseSurveyCreationForm()
        context = {
            'form': pulse_survey_form,
        }
    return render(request=request,
                  template_name='workrecords/create_pulse_survey_page.html',
                  context=context)
