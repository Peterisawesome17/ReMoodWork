# Generated by Django 4.1.5 on 2023-05-08 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workrecords', '0012_alter_fooditem_food_meal_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fooditem',
            name='food_meal_image',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to='meal_item_images/'),
        ),
    ]
