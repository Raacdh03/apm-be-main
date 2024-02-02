from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin

from .models import UserProfile
# from .forms import UserProfileForm

class UserProfileAdmin(admin.ModelAdmin):
  model = UserProfile
  # form = UserProfileForm
  list_display = ['username', 'role', 'status', 'date_joined', 'titles', 'is_active',]
admin.site.register(UserProfile, UserProfileAdmin)
