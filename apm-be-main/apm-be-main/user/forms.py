from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import UserProfile

class UserProfileForm(UserCreationForm):
  class Meta:
    model = UserProfile
    fields = '__all__'
    # widgets = {
    #   'password': forms.PasswordInput(),  # Menggunakan PasswordInput untuk bidang password
    # }