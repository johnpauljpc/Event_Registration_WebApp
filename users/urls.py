from django.urls import path
from .views import *

urlpatterns = [
    path('profile/<int:pk>/', User_Profile.as_view(), name='user-profile'),
    path('my-account/', Account.as_view(), name="account")
]