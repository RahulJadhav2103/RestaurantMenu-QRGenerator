from django import forms
from django.contrib.auth.models import User
from allauth.account.forms import SignupForm

class CustomSignUpForm(SignupForm):
    email = forms.EmailField(
        required=True,
        label='Email',
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your email'
        })
    )
    username = forms.CharField(
        max_length=150,
        label='Username',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter username'
        })
    )
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email and User.objects.filter(email=email).exists():
            raise forms.ValidationError('This email is already registered. Please use a different email or try logging in.')
        return email
    
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if username and User.objects.filter(username=username).exists():
            raise forms.ValidationError('This username is already taken. Please choose a different username.')
        return username


class QRCodeForm(forms.Form):
    restaurant_name=forms.CharField(max_length=50,
                                    label='Restaurant Name',
                                    widget=forms.TextInput(
                                        attrs={
                                            'class':'form-control',
                                            'placeholder':'Enter Name'
                                        }
                                    ))
    url =forms.URLField(max_length=200, 
                        label='Menu URL',
                        widget=forms.URLInput(attrs={
                            'class':'form-control',
                            'placeholder':'Paste a public PDF link here'
                        }))