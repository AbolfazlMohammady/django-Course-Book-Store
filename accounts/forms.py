from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import User



class UserCreationForm(UserCreationForm):
    class Meta:
        model= User
        fields= ('username', 'age', 'email',)


class UserChangeForm(UserChangeForm):
    class Meta:
        model= User
        fields= ('username', 'age', 'email',)
