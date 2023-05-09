from django.shortcuts import render, redirect
from django.http import HttpResponse # Used for testing http response to view web pages of remoodwork's workrecords - Peter
from datetime import datetime # Useful for implementing pulse survey page later in this project - Peter
from workrecords.forms import PulseSurveyCreationForm, MealAssessementCreationForm, \
    FoodItemCreationForm
from users.models import Employee, User, Employer
from django.contrib import messages
from workrecords.models import PulseSurvey, MealPlan, FoodItem, Order
from django.contrib.auth.decorators import login_required, user_passes_test
import re
from django.db.models import Q
from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.urls import reverse

# Create your views here.
# Used for creating a main website of remoodwork and work record logs of an employee- Peter
# Will also be used to create pulse surveys to employees - Peter


def home_view(request):
    '''A view of a home website page of remoodwork'''
    # Only displays a list of pulse survey records from the employee (user)
    # and will also be the main home page of remoodwork for adding few features later on
    pulse_survey_records, employees_with_same_company_name, employer_exists, employee_exists = [None]*4
    company_name_title = ''
    food_item_lists = None
    employer = None
    meal_plan = None
    if request.user.id:
        curr_user = User.objects.get(pk=request.user.id)
        employer_exists, employee_exists = Employer.objects.filter(user=curr_user)\
            , Employee.objects.filter(user=curr_user)
        if employee_exists.exists():
            employee = Employee.objects.get(user=curr_user)
            pulse_survey_records = PulseSurvey.objects.filter(employee=employee)
            meal_plan = MealPlan.objects.filter(employee=employee).first()
        if employer_exists.exists():
            employer = Employer.objects.get(user=curr_user)
            employees_with_same_company_name = Employee.objects.filter(
                user__job_classification_choice = 'EMPLOYEE',
                user__company_name = curr_user.company_name
            )
            company_name_title =  curr_user.company_name
            food_item_lists = FoodItem.objects.filter(employer=employer)
    context =  {
        'user_id': request.user.id,
        'employee_pulse_survey_records': pulse_survey_records,
        'employer_employee_list': employees_with_same_company_name,
        'company_name_title': company_name_title,
        'employer': employer,
        'food_items': food_item_lists,
        'meal_plan': meal_plan
    }
    return render(request=request, template_name='workrecords/home_page.html', context=context)

def pulse_survey_view(request, pk, emp_pk=None):
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
    context = {
        'user_id': pk,
        'pulse_survey_records': pulse_survey_records,
    }
    return render(request=request,
                  template_name='workrecords/pulse_survey_main_page.html',
                  context=context)

def filter_food_item(meal_plan, company_name):
    ''' A helper function to filter food meal items based on employee's
    health info based on their meal planning assessment '''
    food_item_filter = None
    if meal_plan:
        cuisine_text = meal_plan.cuisine
        dietary_restrictions_text = meal_plan.dietary_restrictions
        allergy_text = meal_plan.allergy
        filter_cuisine = re.sub(r'[^\w\s-]+', '', cuisine_text.lower())
        filter_dietary_restrictions = re.sub(r'[^\w\s-]+', '', dietary_restrictions_text.lower())
        filter_allergy = re.sub(r'[^\w\s-]+', '', allergy_text.lower())
        calories = meal_plan.calories
        price = meal_plan.budget
        food_item_filter = FoodItem.objects.filter(Q(price__lte=price) | Q(price__isnull=True),
                                                   cuisine_type__in=filter_cuisine.split(),
                                                   dietary_restrictions__in=filter_dietary_restrictions.split(),
                                                   calories__lte=calories,
                                                   employer__user__company_name=company_name
                                                   ).exclude(allergy__in=filter_allergy.split())
    return food_item_filter

def order_food_meal_item(request, pk, food_pk):
    ''' A view for employees placing their food meal item '''
    employee = get_object_or_404(Employee, user=pk)
    food_item = get_object_or_404(FoodItem, pk=food_pk)
    meal_plan = MealPlan.objects.get(employee=employee)
    url = reverse('remoodwork-meal-plan', kwargs={'pk': pk})
    if request.method == "POST":
        order_meal = request.POST.get('order_meal')
        if order_meal == "yes":
            check_order = Order.objects.filter(employee=employee)
            if not check_order.exists():
                order = Order(employee=employee, meal_plan=meal_plan)
                order.save()
            else:
                order = Order.objects.get(employee=employee, meal_plan=meal_plan)
            order.food_items.add(food_item)
            messages.success(request=request, message='You have successfully placed an ordered'
                                                      f' meal item {food_item.food_name}')
            return redirect(url)
        elif order_meal == "no":
            return redirect(url)
    else:
        return render(
            request=request, template_name='workrecords/order_food_meal_plan.html',
    context={'pk': pk, 'food_pk': food_pk, 'food_item': food_item}
        )

def meal_plan_view(request, pk):
    ''' View for the meal plan '''
    if pk:
        user = User.objects.get(pk=pk)
        employee = Employee.objects.get(user=user)
        meal_plan_record = MealPlan.objects.filter(employee=employee).first()
        food_item_result = filter_food_item(meal_plan_record, user.company_name)
        employee_order_exists = Order.objects.filter(employee=employee)
        if employee_order_exists.exists():
            order = Order.objects.get(employee=employee)
            order = order.food_items.all()
        else:
            order = Order.objects.filter(employee=employee).prefetch_related('food_items')
    context = {
        'user_id': pk,
        'meal_plan_record': meal_plan_record,
        'food_item_lists': food_item_result,
        'order_food': order
    }
    return render(request=request, template_name='workrecords/meal_plan_main_page.html', context=context)

def create_meal_plan_view(request, pk):
    ''' A view controller to create meal plan assessment record made by an employee (user) '''
    user = User.objects.get(pk=pk)
    employee = Employee.objects.get(user=user)
    if request.method == 'POST':
        meal_plan_form = MealAssessementCreationForm(request.POST)
        if meal_plan_form.is_valid():
            meal_plan = meal_plan_form.save(commit=False)
            meal_plan.employee = employee
            meal_plan.save()
            messages.success(request=request, message='Your meal plan has already been created')
            return redirect('remoodwork-meal-plan', pk=pk)
        else:
            context = {
                'form': meal_plan_form
            }
    else:
        meal_plan_form = MealAssessementCreationForm()
        context = {
            'form': meal_plan_form
        }
    return render(request=request,
                  template_name='workrecords/create_meal_plan_page.html',
                  context=context)

def create_food_item_view(request, emp_pk):
    ''' A view controller to create food items produced by an employer (user)'''
    user = User.objects.get(pk=emp_pk)
    employer = Employer.objects.get(user=user)
    if request.method == 'POST':
        food_item_form = FoodItemCreationForm(request.POST, request.FILES)
        if food_item_form.is_valid():
            food_item = food_item_form.save(commit=True)
            food_item.employer = employer
            food_item.save()
            messages.success(request=request, message='Your food item has already been created')
            return redirect('remoodwork-home')
    else:
        food_item_form = FoodItemCreationForm()
        context = {
            'form': food_item_form
        }
    return render(request=request,
                  template_name='workrecords/create_food_item_page.html',
                  context=context)

def create_pulse_survey_view(request, pk):
    ''' A view controller to create pulse surveys produced by an employee (user)'''
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
            return redirect('remoodwork-pulse-survey', pk=pk)
        else:
            context = {
                'form': pulse_survey_form,
            }
    else:
        pulse_survey_form = PulseSurveyCreationForm()
        context = {
            'form': pulse_survey_form,
        }
    return render(request=request,
                  template_name='workrecords/create_pulse_survey_page.html',
                  context=context)
