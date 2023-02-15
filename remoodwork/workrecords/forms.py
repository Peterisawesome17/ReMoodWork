from django import forms
from workrecords.models import PulseSurvey

class PulseSurveyCreationForm(forms.ModelForm):
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