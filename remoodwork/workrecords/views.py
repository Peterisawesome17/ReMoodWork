from django.shortcuts import render
from django.http import HttpResponse # Used for testing http response to view web pages of remoodwork's workrecords - Peter
from datetime import datetime # Useful for implementing pulse survey page later in this project - Peter

# Create your views here.
# Used for creating a main website of remoodwork and work record logs of an employee- Peter
# Will also be used to create pulse surveys to employees - Peter
def home_view(request):
    '''A view of a home website page of remoodwork'''
    # More details will be added later on
    # Default return to check an http reponse of a web page
    return render(request=request, template_name='workrecords/home_page.html', context={})

def pulse_survey_view(request):
    '''A view of a pulse survey page where employee creates their work/activity record logs'''
    #Update 1: Will be used to print out today's date of a work/activity record logs of an employee later on
    date_today = datetime.today()
    # {{date_today}} in the templates (later on) for context - Peter
    return HttpResponse('<head>'
                        '<title>ReMoodWork</title>'
                        '</head>'
                        '<body>'
                        '<h1>ReMoodWork Pulse Survey</h1>'
                        f"<p>Today's date {date_today}</p>"
                        '</body>'
                        )
