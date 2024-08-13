from django.urls import path
from .views import *

urlpatterns = [
    path('register/', userRegister, name="register"),
    path('login/', userLogin, name="userlogin"),
    path('logout/', userLogout, name="userlogout"),
    path('password_change/', passwordChange, name="password_change"),
    path('account_delete/', accountDelete, name="account_delete"),
]