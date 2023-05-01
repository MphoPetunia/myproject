from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('name', 'email')
    
    name = forms.CharField(max_length=50, required=True)
    email = forms.EmailField(required=True)
