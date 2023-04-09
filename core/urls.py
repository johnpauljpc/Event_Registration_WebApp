from django.urls import path
from .views import *

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('event/<int:pk>/', EventView.as_view(), name='event')
]