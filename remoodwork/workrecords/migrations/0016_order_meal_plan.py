# Generated by Django 4.1.5 on 2023-05-08 05:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('workrecords', '0015_alter_fooditem_food_meal_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='meal_plan',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='workrecords.mealplan'),
        ),
    ]
