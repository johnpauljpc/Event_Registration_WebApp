from django.urls import path
from .views import *

urlpatterns = [
    path('profile/<pk>/', User_Profile.as_view(), name='user-profile'),
    path('my-account/', Account.as_view(), name="account"),
    path('edit-account/', EditAccount.as_view(), name="edit-account"),
    path('change-password/<uuid:id>/', ChangePassword.as_view(), name="change-password"),
    path('register/', signUpPage, name="register"),
    path('login/', loginPage, name="login"),
    path('logout/', logoutView, name="logout"),
]