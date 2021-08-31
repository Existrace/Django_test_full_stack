from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError


class UserLoginForm(forms.Form):
    """Form to be used to log users in"""

    username = forms.CharField(
        label="Nom d'utilisateur"
    )
    password = forms.CharField(
        label="Mot de passe",
        widget=forms.PasswordInput)


class UserRegisterForm(UserCreationForm):
    """Form used to register a new user"""

    password1 = forms.CharField(
        label="Mot de passe",
        widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="Confirmation mot de passe",
        widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email', 'username', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if User.objects.filter(email=email).exclude(username=username):
            raise forms.ValidationError("L'adresse mail doit être unique")
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if not password1 or not password2:
            raise ValidationError("Le mot de passe est obligatoire")

        if password1 != password2:
            raise ValidationError("Les mots de passes ne correspondent pas")

        return password2


class Add_booking(forms.Form):
    title = forms.CharField(
        label="Nom de réservation"
    )

    # CONTINUER CE FORM ULTERIEUREMENT

