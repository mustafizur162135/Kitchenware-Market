from django import forms

class UploadForm(forms.Form):
    name=forms.CharField()
    price=forms.DecimalField(widget=forms.TextInput)
    qnt=forms.DecimalField(widget=forms.TextInput)
    upldate=forms.DateField()
    image=forms.FileField()

class UpdateForm(forms.Form):
    pid=forms.IntegerField(widget=forms.TextInput)
    name=forms.CharField()
    price=forms.DecimalField(widget=forms.TextInput)
    qnt=forms.DecimalField(widget=forms.TextInput)
    upldate=forms.DateField()
