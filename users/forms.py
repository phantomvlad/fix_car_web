from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from allauth.account.forms import LoginForm, SignupForm
from django import forms
from phonenumber_field.formfields import PhoneNumberField

class CustomUserCreationForm(UserCreationForm):
    slug = forms.CharField(max_length=150)

    class Meta(UserCreationForm):
        model = get_user_model()
        fields=('email', 'username',)

class CustomUserChangeForm(UserChangeForm):
    slug = forms.CharField(max_length=150)
    class Meta(UserChangeForm):
        model = get_user_model()
        fields = ('email', 'username',)

class CustomUserSignupForm(SignupForm):
    class Meta(UserChangeForm):
        model = get_user_model()
        fields = ('email', 'username', 'password')

class CustomUserLoginForm(LoginForm):
    def login(self, *args, **kwargs):
        return super(CustomUserLoginForm,self).login(*args, **kwargs)