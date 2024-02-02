from rest_framework import routers, serializers, viewsets
from .models import UserProfile

# Serializers define the API representation.
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['username', 'role', 'status', 'first_name', 'last_name', 'email', 'is_staff']

