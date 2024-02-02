from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

# Role Choices
class UserRoleChoice(models.TextChoices):
  PM = "PM", _("Project Manager")
  SALES = "SALES", _("Sales")
  ENGINEER = "ENGINEER", _("Engineer")
  ADMIN = "ADMIN", _("Admin Tender")

class UserGenderChoice(models.TextChoices):
  MALE = "M", _("Male")
  FEMALE = "F", _("Female")

class UserStatusChoice(models.TextChoices):
  INTERNAL = "internal", _("Internal")
  EXTERNAL = "external", _("External")

# Create your models here.
class UserProfile(AbstractUser):
  role = models.CharField(max_length=20, choices=UserRoleChoice.choices)
  status = models.CharField(blank=True, max_length=10, 
                            choices=UserStatusChoice.choices, default=UserStatusChoice.INTERNAL)
  is_active = models.BooleanField(blank=True, default=True)

  phone = models.CharField(max_length=20, blank=True)
  
  # technical_skill 
  photo = models.ImageField(blank=True) 

  address = models.TextField(blank=True)

  # short_bio text
  gender = models.CharField(max_length=1, choices=UserGenderChoice.choices)
  department = models.CharField(max_length=50,  blank=True) # IT
  position = models.CharField(max_length=50, blank=True) # Engineer
  titles = models.CharField(max_length=50, blank=True) # Frontend

  # Default
  created_at = models.DateTimeField(db_index=True, default=timezone.now)
  updated_at = models.DateTimeField(auto_now=True)

  # linkedin_profile varchar
  # github_profile varchar
  # additional_info text

  # date_joined date
  # last_login datetime
  def __str__(self):
    return self.username
  
  class Meta:
    verbose_name = 'User profile'
    db_table = 'apm_userprofile'
    ordering = ['-created_at']
    indexes = [ models.Index(fields=['-created_at']), ]

  