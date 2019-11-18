from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User

# register the User model
admin.site.register(User, UserAdmin)


# Custom AdminSite
class AdminSite(admin.AdminSite):
    admin.AdminSite.site_header = 'Wunderman Thompson'
    admin.AdminSite.site_title = admin.AdminSite.site_header
