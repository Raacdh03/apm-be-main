from django.contrib import admin

from .models import UserProfile

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['username', 'role', 'status', 'date_joined', 'titles', 'is_active',]
admin.site.register(UserProfile, UserProfileAdmin)
