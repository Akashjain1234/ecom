from multiprocessing.spawn import import_main_path
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .models import AddressModel



class SignupForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control input-lg'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control input-lg'}))

    class Meta:
        model = User
        fields = ["username","email","password1","password2"]
        widgets = {
            'username':forms.TextInput(attrs={'class':'form-control input-lg'}),
            'email':forms.EmailInput(attrs={'class':'form-control input-lg'}),
        }

class AddressForm(forms.ModelForm):
    class Meta:
        model = AddressModel
        fields = ["first_name","last_name","email","address","phone"]
        widgets= { 
            'first_name' : forms.TextInput(attrs={'class':'form-control input-lg'}),
            'last_name' : forms.TextInput(attrs={'class':'form-control input-lg'}),
            'email' : forms.EmailInput(attrs={'class':'form-control input-lg'}),
            'address' : forms.TextInput(attrs={'class':'form-control input-lg'}),
            'phone' : forms.NumberInput(attrs={'class':'form-control input-lg'})
            }

    