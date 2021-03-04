from django import forms

class RegisterForm(forms.Form):
    email=forms.EmailField()
    pw=forms.CharField(widget=forms.PasswordInput)


class LoginForm(forms.Form):
    email=forms.EmailField()
    pw=forms.CharField(widget=forms.PasswordInput)
