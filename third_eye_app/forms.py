from django import forms
from .models import Profile, Business

class Profile_Form(forms.ModelForm):
    class meta:
        model = Profile
        fields = ('name', 'email')
    

class Business_Form(forms.ModelForm):
    class meta:
        model = Business
        fields = ('name', 'email')
      