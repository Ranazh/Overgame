from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from accounts.models import UserProfile


class UserProfileForm(UserCreationForm):
    class Meta:
        model = UserProfile
        fields = ('username', 'first_name', 'last_name',
                  'password1', 'password2',
                  'email')


class EditProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = (
            'username', 'first_name', 'last_name', 'email'
        )

