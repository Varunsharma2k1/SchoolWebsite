from django import forms

from .models import *

class CareerForm(forms.ModelForm):
    class Meta:
        model = Career
        fields = "__all__"
        widgets={
            'Name':forms.TextInput(attrs={'class':'inputs', 'placeholder':'Enter Name'}),
            'email':forms.EmailInput(attrs={'class':'inputs','placeholder':'Enter Email'}),
            'phone':forms.NumberInput(attrs={'class':'inputs','placeholder':'Enter Phone number'}),
            'post':forms.Select(attrs={'class':'inputs'}),
            'resume':forms.FileInput(),
            
        }  

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = "__all__"
        widgets={
            'FirstName':forms.TextInput(attrs={'class':'inputs', 'placeholder':'Enter First Name'}),
            'LastName':forms.TextInput(attrs={'class':'inputs', 'placeholder':'Enter Last Name'}),
            'email':forms.EmailInput(attrs={'class':'inputs','placeholder':'Enter Email'}),
            'LastSchool':forms.TextInput(attrs={'class':'inputs', 'placeholder':'Last School Attended (if none type none)'}),
            'FatherName':forms.TextInput(attrs={'class':'inputs', 'placeholder':'Enter Father Name'}),
            'phone':forms.NumberInput(attrs={'class':'inputs','placeholder':'Enter Phone number'}),
            'Address':forms.TextInput(attrs={'class':'inputs', 'placeholder':'Enter Address'}),
            'SiblingName':forms.TextInput(attrs={'class':'inputs', 'placeholder':'Enter sibling name if any'}),
            'Class':forms.TextInput(attrs={'class':'inputs', 'placeholder':'Enter class of sibling if any'}),
        }   