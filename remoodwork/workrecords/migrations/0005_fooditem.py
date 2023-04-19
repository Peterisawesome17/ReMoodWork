# Generated by Django 4.1.5 on 2023-04-19 05:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_employer'),
        ('workrecords', '0004_rename_cusine_mealplan_cuisine'),
    ]

    operations = [
        migrations.CreateModel(
            name='FoodItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food_name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('price', models.FloatField()),
                ('cuisine_type', models.CharField(choices=[('italian', 'Italian'), ('american', 'American'), ('mexican', 'Mexican'), ('asian', 'Asian')], max_length=30)),
                ('food_item_type', models.CharField(choices=[('restaurant', 'Restaurant Item'), ('recipe', 'Recipe')], max_length=30)),
                ('recipe_url', models.URLField(blank=True, null=True)),
                ('restaurant_name', models.CharField(blank=True, max_length=100, null=True)),
                ('calories', models.PositiveIntegerField()),
                ('dietary_restrictions', models.CharField(max_length=100)),
                ('allergy', models.CharField(max_length=100)),
                ('employer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.employer')),
            ],
        ),
    ]