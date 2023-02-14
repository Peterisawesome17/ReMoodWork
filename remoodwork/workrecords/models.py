from django.db import models
from users.models import Employee

# Create your models here.

class PulseSurvey(models.Model):
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
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
