from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.forms import ModelForm, fields
from django import forms


# creating a from from django builtin form for user registration
class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

# overriding the builtin form since it had a bug that did'nt show the inactive user error message
class LogInForm(AuthenticationForm):
    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username is not None and password:
            self.user_cache = authenticate(self.request, username=username, password=password)
            if self.user_cache is None:
                try:
                    user_temp = User.objects.get(username=username)
                except:
                    user_temp = None
                
                if user_temp is not None:
                    self.confirm_login_allowed(user_temp)
                else:
                    raise forms.ValidationError(
                        self.error_messages['invalid_login'],
                        code='invalid_login',
                        params={'username': self.username_field.verbose_name},
                    )

        return self.cleaned_data