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