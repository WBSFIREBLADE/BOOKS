from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models import Customer

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username']


class UserProfileForm(UserChangeForm):
    password =None
    class Meta:
        model = User
        fields =['username','first_name','email','date_joined','last_login']
        widgets= {'username':forms.TextInput(attrs={'class':'form-control'}),
                  'first_name':forms.TextInput(attrs={'class':'form-control'}),
                  'email':forms.TextInput(attrs={'class':'form-control'}),
                  'date_joined':forms.DateInput(attrs={'class':'form-control','type': 'date'}),
                  'last_login':forms.DateInput(attrs={'class':'form-control','type': 'date'}),
                  }

class AdminProfileForm(UserChangeForm):
    password =None
    class Meta:
        model = User
        fields = '__all__'
        widgets= {'username':forms.TextInput(attrs={'class':'form-control'}),
                  'email':forms.TextInput(attrs={'class':'form-control'}),
                  'first_name':forms.TextInput(attrs={'class':'form-control'}),
                  }

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields=['name','address','city','state','pincode']
        labels ={'name':'Full Name'}
        widgets= {'name':forms.TextInput(attrs={'class':'form-control'}),
                  'address':forms.TextInput(attrs={'class':'form-control'}),
                  'city':forms.TextInput(attrs={'class':'form-control'}),
                  'state':forms.Select(attrs={'class':'form-control'}),
                  'pincode':forms.NumberInput(attrs={'class':'form-control'}),
                  }