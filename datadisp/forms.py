from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class CreateUserForm(UserCreationForm):
    """
    Replace CreateUserForm from django with custom fields, 
    nevertheless kept settings for Authentification and Security
    """
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        """
        Widget permet l'utilisation 
        """
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom d\'utilisateur'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Votre e-mail'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Votre mot de passe'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirmez votre mot de passe'})
        }
