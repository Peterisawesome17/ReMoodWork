# Generated by Django 4.1.5 on 2023-04-23 00:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workrecords', '0007_alter_fooditem_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fooditem',
            name='allergy',
            field=models.CharField(choices=[('wheat', 'Wheat'), ('peanuts', 'Peanuts'), ('shellfish', 'Shellfish'), ('beef', 'Beef')], max_length=100),
        ),
        migrations.AlterField(
            model_name='fooditem',
            name='dietary_restrictions',
            field=models.CharField(choices=[('gluten-free', 'Gluten-free'), ('vegetarian', 'Vegetarian')], max_length=100),
        ),
    ]
