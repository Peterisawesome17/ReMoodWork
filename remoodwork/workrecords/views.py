from django.shortcuts import render
from django.http import HttpResponse #Used <Continue>

# Create your views here.
# Used for creating a main website of remoodwork and work record logs of an employee- Peter
# Will also be used to create pulse surveys to employees - Peter
def home_view(request):
    '''A view of a home website page of remoodwork'''
    # More details will be added later on
    # Default return to check an http reponse of a web page
    return HttpResponse('<h1>ReMoodWork Home</h1>')