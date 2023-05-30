from django.urls import path
from .views import *

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('event/<uuid:pk>/', EventView.as_view(), name='event'),
    path('confirm-registration/event/<int:pk>/', Confirm_Event_Registration.as_view(), name="confirm-event"),
    path('submit-project/uuid:pk>/', project_submission, name='project-submission'),
    path('update-project/<uuid:pk>/', UpdateSubmission, name='update-submission'),
]