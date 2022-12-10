from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import User

class UserRegistrationForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

class ProfileForm(ModelForm):
	class Meta:
		model = User
		fields = ['first_name', 'last_name', 'password', 'about']