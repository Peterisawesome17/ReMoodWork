from django.contrib import admin
from users.models import User

# Register your models here.
# Must provide a User register for the admin page of remoodwork
admin.site.register(User)
