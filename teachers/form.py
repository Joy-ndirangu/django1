from . models import  CustomUser

from django.contrib.auth.forms import UserChangeForm, UserCreationForm


#django forms

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ['username', 'year','email', 'password1','password2']

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields

