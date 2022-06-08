from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import password_validation


class SignupForm(UserCreationForm):
    email = forms.CharField(max_length=50, required=True)
    full_name = forms.CharField(max_length=50, required=True)
    password2 = None

    class Meta:
        model = User
        fields = ('email', 'full_name', 'username', 'password1')

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        try:
            password_validation.validate_password(password1, self.instance)
        except forms.ValidationError as error:
            self.add_error('password1', error)
        return password1


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')
