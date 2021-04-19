from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        labels = {
            'username': '',
            'email': '',
        }
        help_texts = {
            'username': '',
            'email': '',
        }
        widgets = {
            'username': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'style': 'font-size: 20px;',
                    'placeholder': 'Username'
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control', 
                    'style': 'font-size: 20px;',
                    'placeholder': 'Email Address'
                }
            )
        }
    def __init__(self, *args, **kwargs):

        super(UserCreationForm, self).__init__(*args, **kwargs)

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'

        self.fields['password1'].widget.attrs['style'] = 'font-size: 20px;'
        self.fields['password2'].widget.attrs['style'] = 'font-size: 20px;'

        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password2'].widget.attrs['placeholder'] = 'Re-enter Password'

    def clean(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if User.objects.filter(email=email).exists():
            raise ValidationError('Email Already Exists')
        if User.objects.filter(username=username).exists():
            raise ValidationError('Username Already Taken')
        return self.cleaned_data