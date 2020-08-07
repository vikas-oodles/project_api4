from django.urls import path
from .views import UserRegistrationApiView
app_name = 'myapi'

urlpatterns = [
    path('register/',UserRegistrationApiView.as_view(),name='userregistration_api'),
]