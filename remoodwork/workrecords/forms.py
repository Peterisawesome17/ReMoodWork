from django import forms
from workrecords.models import PulseSurvey, MealPlan, FoodItem

class FoodItemCreationForm(forms.ModelForm):
    ''' Used for allowing employers to create a food item with a couple of required fields '''
    class Meta:
        model = FoodItem
        fields = ['food_name', 'description', 'price', 'cuisine_type', 'food_item_type',
                  'recipe_url', 'restaurant_name', 'calories', 'dietary_restrictions',
                  'allergy', 'food_meal_image']
        labels = {
            'food_name': 'Enter the name of the food',
            'description': 'Is there any description you would like to discuss contents on the food?',
            'price': 'Is there a price range you would like to include on a food item?',
            'cuisine_type': 'Which cuisine works best for this food item?',
            'food_item_type': 'Is this food item a food recipe or restaurant',
            'recipe_url': 'If recipe, please enter the url of a recipe',
            'restaurant_name': 'If restaurant, please enter the name of the restaurant',
            'calories': 'What are calories of this food item?',
            'dietary_restrictions': 'Which dietary restriction works best for this food item?',
            'allergy': 'What allergy contains in this food?',
            'food_meal_image': 'Images you want to upload for a food item?'
        }

class MealAssessementCreationForm(forms.ModelForm):
    ''' Used for allowing employees to create their meal planning assessments with a
    couple of required fields '''
    class Meta:
        model = MealPlan
        fields = ["calories", "dietary_restrictions", "goal", "allergy", "budget", "cuisine"]
        labels = {
            "calories": "Enter your calorie diet",
            "dietary_restrictions": "What is your dietary restrictions?",
            "goal": "What is your expected health measurement goal?",
            "allergy": "Do you have any food allergies?",
            "budget": "What is your current budget?",
            "cuisine": "What is the cuisine you are looking for?"
        }

class PulseSurveyCreationForm(forms.ModelForm):
    ''' Used for allowing employees to create their pulse survey with
    a couple of required fields '''
    class Meta:
        model = PulseSurvey
        fields = ["activity_name", "activity_type", "num_hours", "emotional_rate_status",
                  "activity_description", "work_stressor_status"]
        labels = {
            "activity_name": "Your activity name",
            "activity_type": "What was your activity type?",
            "num_hours": "How many hours did you spend on this activity?",
            "emotional_rate_status": "How would you rate your emotional scale on this activity?",
            "activity_description": "Any descriptions you want to write about your activity?",
            "work_stressor_status": "Were there any work-related stress issues you had on your activity?"
        }

    def is_valid(self):
        is_valid = super().is_valid()
        if is_valid:
            # This is where the implementation of checking if an activity name exists
            # from one of the pulse surveys that an employee already created from a database table
            # of remoodwork
            # Verify to see if an activity name exists from one of the pulse surveys created
            # by an employee
            activity_name = self.cleaned_data.get('activity_name')
            pulse_survey_record_check = PulseSurvey.objects.filter(activity_name=activity_name)
            if pulse_survey_record_check.exists():
                self.add_error('activity_name', 'This activity name already exists '
                                                'from one of your pulse survey records.')
                is_valid = False
        return is_valid