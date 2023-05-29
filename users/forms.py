from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import User

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['name', 'email', 'bio', 'password1', 'password2',  'hackthon_participant']
        