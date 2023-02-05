from django.shortcuts import render, HttpResponse
# from django.contrib.auth.forms import UserCreationForm
from users.forms import UserRegistrationForm

# Create your views here.
def register_view(request):
    form = UserRegistrationForm()
    context = {
        'form' : form,
    }
    # return HttpResponse('<h1>Welcome to the employees registration page!</h1>')
    return render(request=request, template_name='users/register_page.html', context=context)