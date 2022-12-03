from django import forms

class ProfileForm(forms.Form):
    nama = forms.CharField(label='Your display name', max_length=20)