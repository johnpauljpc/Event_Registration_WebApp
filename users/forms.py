from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
# from .models import User
from django.contrib.auth import get_user_model

User = get_user_model()
class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['name', 'email', 'avatar', 'bio', 'password1', 'password2',  'hackthon_participant']

        # widget ={
        #     ''
        # }
        # widgets = {
		# 	'name':forms.TextInput(attrs={ 'class':'form-control ', 'id':'name', }),

class EditAccountForm(ModelForm):
    class Meta:
        model = User
        fields = ['name', 'email', 'username', 'avatar', 'bio']