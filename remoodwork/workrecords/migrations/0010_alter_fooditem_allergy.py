# Generated by Django 4.1.5 on 2023-05-01 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workrecords', '0009_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fooditem',
            name='allergy',
            field=models.CharField(choices=[('wheat', 'Wheat'), ('peanuts', 'Peanuts'), ('shellfish', 'Shellfish'), ('beef', 'Beef'), ('soy', 'Soy')], max_length=100),
        ),
    ]
