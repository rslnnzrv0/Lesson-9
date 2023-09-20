from django.core.validators import MinLengthValidator, EmailValidator, RegexValidator, MinValueValidator
from django import forms
from .models import Visitor


class RegistrationForm(forms.ModelForm):
    name = forms.CharField(
        validators=[MinLengthValidator(2)],
        widget=forms.TextInput(attrs={'placeholder': 'Enter your name'})
    )
    email = forms.EmailField(
        validators=[EmailValidator(message='Please enter a valid email address.')],
        widget=forms.EmailInput(attrs={'placeholder': 'Enter your email'})
    )
    age = forms.IntegerField(
        validators=[MinValueValidator(18)],
        widget=forms.NumberInput(attrs={'placeholder': 'Enter your age'})
    )
    gender = forms.ChoiceField(
        choices=[('male', 'Male'), ('female', 'Female')],
        widget=forms.RadioSelect
    )
    address = forms.CharField(
        validators=[MinLengthValidator(5)],
        widget=forms.TextInput(attrs={'placeholder': 'Enter your address'})
    )
    phone = forms.CharField(
        validators=[RegexValidator(r'^\+998\d{9}$', message='Please enter a valid phone number.')],
        widget=forms.TextInput(attrs={'placeholder': 'Enter your phone number'})
    )
    occupation = forms.CharField(
        validators=[MinLengthValidator(2)],
        widget=forms.TextInput(attrs={'placeholder': 'Enter your occupation'})
    )
    membership_type = forms.ChoiceField(
        choices=[('basic', 'Basic'), ('premium', 'Premium')],
        widget=forms.Select
    )
    username = forms.CharField(
        validators=[MinLengthValidator(5)],
        widget=forms.TextInput(attrs={'placeholder': 'Enter a username'})
    )
    password = forms.CharField(
        validators=[MinLengthValidator(8)],
        widget=forms.PasswordInput(attrs={'placeholder': 'Enter a password'})
    )

    class Meta:
        model = Visitor
        fields = ['name', 'email', 'age', 'gender', 'address', 'phone', 'occupation', 'membership_type', 'username',
                  'password']
