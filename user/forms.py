from django import forms
from django.forms import ModelForm

class LoginForm(forms.Form):
    username = forms.CharField(widget= forms.TextInput(attrs={'class':'input100','name':'Nome',
            'placeholder':'Nome'}))
    password = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'class':'input100','name':'password',
            'placeholder':'Palavra passe'}))


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=50, label="Nome do usuários")
    password = forms.CharField(max_length=20, label="Password", widget=forms.PasswordInput)
    confirm = forms.CharField(max_length=20, label="Verify Password", widget=forms.PasswordInput)
    
    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        confirm = self.cleaned_data.get("confirm")

        if password and confirm and password != confirm:
            raise forms.ValidationError("As senhas não correspondem")

        values = {
            "username": username,
            "password": password
        }
        return values


# class MessageForm(ModelForm):
#     class Meta:
#         model = Message
#         fields = ['nome', 'email', 'message']


