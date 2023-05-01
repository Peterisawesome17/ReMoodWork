from django.db import models
from users.models import Employee, Employer

# Create your models here.
class MealPlan(models.Model):
    calories = models.PositiveIntegerField()
    dietary_restrictions = models.CharField(max_length=100)
    goal = models.CharField(max_length=100, blank=True)
    allergy = models.CharField(max_length=100)
    budget = models.FloatField()
    cuisine = models.CharField(max_length=100)
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE)

    def __str__(self):
        return f'employee: {self.employee}'

class PulseSurvey(models.Model):
    ''' A PulseSurvey model contains about 6 to 8 attribute fields needed to be created
    in the database table of remoodwork '''
    ACTIVITY_TYPE_CHOICES = (
        ("WT", "Work task"),
        ("TB", "Take a break"),
        ("DFV", "Day off/vacation")
    )
    EMOJI_STATUS_CHOICE = (
        ("happy", "\N{grinning face}"),
        ("tired", "\N{tired face}"),
        ("illness", "\N{face with thermometer}"),
        ("taking_break_or_vacation", "\N{smiling face with sunglasses}"),
        ("sleeping", "\N{sleeping face}"),
        ("need_help", "\N{confused face}"),
        ("upset", "\N{crying face}"),
        ("normal", "\N{neutral face}")
    )
    WORK_STRESSOR_STATUS_CHOICE = (
        ('YES', 'Yes'),
        ('NO', 'No')
    )
    activity_name = models.CharField(max_length=205)
    activity_type = models.CharField(max_length=20, choices=ACTIVITY_TYPE_CHOICES)
    num_hours = models.CharField(max_length=10)
    emotional_rate_status = models.CharField(max_length=35, choices=EMOJI_STATUS_CHOICE)
    activity_description = models.TextField(blank=True, null=True)
    work_stressor_status = models.CharField(max_length=5, choices=WORK_STRESSOR_STATUS_CHOICE)
    activity_created = models.DateField(auto_now_add=True)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='pulse_survey')

    def __str__(self):
        return f'Pulse Survey Record: {self.activity_name}'

class FoodItem(models.Model):
    CUISINE_CHOICES = [
        ('italian', 'Italian'),
        ('american', 'American'),
        ('mexican', 'Mexican'),
        ('asian', 'Asian'),
    ]

    DIETARY_RESTRICTION_CHOICES = [
        ('gluten-free', 'Gluten-free'),
        ('vegetarian', 'Vegetarian')
    ]

    ALLERGY_CHOICES = [
        ('wheat', 'Wheat'),
        ('peanuts', 'Peanuts'),
        ('shellfish', 'Shellfish'),
        ('beef', 'Beef'),
        ('soy', 'Soy')
    ]

    TYPE_CHOICES = [
        ('restaurant', 'Restaurant'),
        ('recipe', 'Recipe'),
    ]

    food_name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField(null=True, blank=True)
    cuisine_type = models.CharField(max_length=30, choices=CUISINE_CHOICES)
    food_item_type = models.CharField(max_length=30, choices=TYPE_CHOICES)
    recipe_url = models.URLField(blank=True, null=True)
    restaurant_name = models.CharField(max_length=100, blank=True, null=True)
    calories = models.PositiveIntegerField()
    dietary_restrictions = models.CharField(max_length=100, choices=DIETARY_RESTRICTION_CHOICES)
    allergy = models.CharField(max_length=100, choices=ALLERGY_CHOICES)
    employer = models.ForeignKey(Employer, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f'Food name: {self.food_name}, pk: {self.pk}'

class Order(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    food_items = models.ManyToManyField(FoodItem, related_name='orders')

    def __str__(self):
        return f'Order Food item from ({self.employee}), pk {self.pk}'
