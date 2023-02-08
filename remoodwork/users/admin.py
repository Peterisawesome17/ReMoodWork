from django.contrib import admin
from users.models import User, Employee

# Register your models here.
# Must provide a User and Employee register for the admin page of remoodwork
admin.site.register(User)
admin.site.register(Employee)
