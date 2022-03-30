from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import *



class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['first_name','last_name','username', 'password1','password2','phone']

class SubscriptionForm(ModelForm):
	class Meta:
		model = Subscription
		fields = "__all__"