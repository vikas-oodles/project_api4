from django.urls import path
from .views import UserRegistrationApiView, UserLoginView, UserApiView
app_name = 'myapi'

urlpatterns = [
    path('register/',UserRegistrationApiView.as_view(),name='userregistration_api'),
    path('login/',UserLoginView.as_view(),name='userlogin_api'),
    path('userlist/',UserApiView.as_view(), name='userlist'),
]