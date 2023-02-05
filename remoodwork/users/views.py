from django.shortcuts import render, HttpResponse, redirect
# from django.contrib.auth.forms import UserCreationForm
from users.forms import UserRegistrationForm
from django.contrib import messages

# Create your views here.
def register_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request=request, message=f'Account created for {username}')
            return redirect('remoodwork-home')
        else:
            context = {
                'form': form,
            }
            # return HttpResponse('<h1>Welcome to the employees registration page!</h1>')
            return render(request=request, template_name='users/register_page.html', context=context)
    else:
        form = UserRegistrationForm()
        context = {
        'form' : form,
        }
        # return HttpResponse('<h1>Welcome to the employees registration page!</h1>')
        return render(request=request, template_name='users/register_page.html', context=context)