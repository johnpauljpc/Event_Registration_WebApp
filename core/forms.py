from django.forms import ModelForm
from .models import Submission

class submissionForm(ModelForm):
    class Meta:
        model = Submission
        fields = ['details']