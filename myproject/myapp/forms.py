import uuid
from django import forms
from .models import Episode
from allauth.account.forms import SignupForm, LoginForm

class EpisodeForm(forms.ModelForm):
    class Meta:
        model = Episode
        fields = ['title', 'description', 'audio_file', 'publication_date']
<<<<<<< HEAD
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'audio_file': forms.FileInput(attrs={'class': 'form-control'}),
            'publication_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if "proibido" in title:
            raise forms.ValidationError("Palavra 'proibido' não é permitida no título.")
        return title


class CustomSignupForm(SignupForm):
    username = forms.CharField(max_length=30, label='Nome de Usuário')
    first_name = forms.CharField(max_length=30, label='Nome')
    last_name = forms.CharField(max_length=30, label='Sobrenome')
    email = forms.EmailField(max_length=254, label='E-mail')
    password1 = forms.CharField(label='Senha', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirme sua senha', widget=forms.PasswordInput)

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.username = self.cleaned_data['username']  # Usar o username fornecido
        user.save()
        return user


class CustomSigninForm(LoginForm):
    email = forms.EmailField(max_length=254, label='Email')
    password = forms.CharField(label='Senha', widget=forms.PasswordInput)
    
class SearchForm(forms.Form):
    query = forms.CharField(max_length=100, label='Search')
=======


from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
>>>>>>> ad36b6214467c0d387e2d33aa9d24c693721e329
