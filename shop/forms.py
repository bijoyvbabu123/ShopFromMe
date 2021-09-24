from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError
from django.forms import ModelForm, fields
from django import forms


# creating a from from django builtin form for user registration
class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

# overriding the builtin form since it had a bug that did'nt show proper error messages
class LogInForm(AuthenticationForm):
    error_messages = {
        'invalid': '''No Account Exists !!''',
        'inactive': '''This account is Inactive.''',
        'incorrect': '''Incorrect Password !!''',
    }

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
                    if not user_temp.is_active:
                        raise ValidationError(
                        self.error_messages['inactive'],
                        code='inactive',
                    )
                    else:
                        raise ValidationError(
                        self.error_messages['incorrect'],
                        code='incorrect',
                    )
                    
                else:
                    raise ValidationError(
                        self.error_messages['invalid'],
                        code='invalid',
                    )

        return self.cleaned_data