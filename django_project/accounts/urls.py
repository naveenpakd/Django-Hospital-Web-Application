from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('register' , register_attempt , name="register_attempt"),
    path('login' , login_attempt , name="login"),
    path('logout',logout,name='logout'),
    path('token' , token_send , name="token"),
    path('success' , success , name='success'),
    path('verify/<auth_token>' , verify , name="verify"),
    path('error' , error_page , name="error"),
    path('forget-password' , ForgetPassword , name="forget_password"),
    path('change-password/<token>/' , ChangePassword , name="change_password"),
    path('password_update',PasswordUpdate,name='password_update'),
    path('edit',Edit,name='edit'),
    path('update-email/', update_email, name='update_email'),
    path('verify-email/', verify_email, name='verify_email'),

]
