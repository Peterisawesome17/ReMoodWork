from django.contrib import admin
from users.models import User, Employee

# Register your models here.
# Must provide a User and Employee register for the admin page of remoodwork
# A User Admin class will be added later in this project.

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('user', )

admin.site.register(User)
admin.site.register(Employee, EmployeeAdmin)
