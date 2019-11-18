from django import forms
from django.db.models import Q
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import User


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
        )


class SignInForm(AuthenticationForm):
    def clean(self):
        username = self.cleaned_data.get('username')

        try:
            if '@' in username:
                query = (
                    Q(username=username) |
                    Q(email=username)
                )
                # Query for username or email before of 'Sign In'
                user = User.objects.get(query)

                if user is not None:
                    self.cleaned_data['username'] = user.username

        except User.DoesNotExist:
            pass

        return super().clean()
