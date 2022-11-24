from django import forms
from AppTwo.models import UserLogin

class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = UserLogin
        fields = ['name', 'surname', 'email', 'password']