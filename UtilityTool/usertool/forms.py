from .models import UserBase
from django.forms import ModelForm, TextInput, PasswordInput, EmailInput


class UserBaseForm(ModelForm):
    class Meta:
        model = UserBase
        fields = ['email', 'nickname', 'password']

        widgets = {
            "email": EmailInput(attrs={
                'class': 'form-email inp-form-reg',
                'placeholder': 'Email'
            }),
            "nickname": TextInput(attrs={
                'class': 'form-nickname inp-form-reg',
                'placeholder': 'Nickname'
            }),
            "password": PasswordInput(attrs={
                'class': 'form-password inp-form-reg',
                'placeholder': 'Password'
            }),
        }
