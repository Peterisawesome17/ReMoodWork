from django.contrib import admin
from users.models import User, Employee, Employer

# Register your models here.
# Must provide a User and Employee register for the admin page of remoodwork
# A User Admin class will be added later in this project.

class EmpAdmin(admin.ModelAdmin):
    list_display = ('user', )

admin.site.register(User)
admin.site.register(Employee, EmpAdmin)
admin.site.register(Employer, EmpAdmin)
