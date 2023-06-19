from django.urls import path
from .views import *

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('event/<uuid:pk>/', EventView.as_view(), name='event'),
    path('confirm-registration/event/<uuid:pk>/', Confirm_Event_Registration.as_view(), name="confirm-event"),
    path('submit-project/<uuid:id>/', project_submission, name='project-submission'),
    path('update-project/<uuid:id>/', UpdateSubmission, name='update-submission'),
]