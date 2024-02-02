from django.urls import path

from . import views_api

urlpatterns = [
    path('', views_api.UserProfileListCreate.as_view(), name='user-list-create'),
]