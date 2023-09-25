from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from allauth.account.forms import LoginForm, SignupForm

from phonenumber_field.formfields import PhoneNumberField

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = get_user_model()
        fields=('email', 'username', 'phone')

class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm):
        model = get_user_model()
        fields = ('email', 'username', 'phone')

class CustomUserSignupForm(SignupForm):
    phone = PhoneNumberField(region='RU')

class CustomUserLoginForm(LoginForm):
    def login(self, *args, **kwargs):
        return super(CustomUserLoginForm,self).login(*args, **kwargs)