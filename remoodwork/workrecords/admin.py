from django.contrib import admin
from workrecords.models import PulseSurvey, MealPlan

# Register your models here.
# Must provide a PulseSurvey register for the admin page of remoodwork
# More models will be registered later
admin.site.register(PulseSurvey)
admin.site.register(MealPlan)