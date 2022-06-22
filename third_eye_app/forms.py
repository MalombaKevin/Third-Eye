from django import forms
from .models import Jirani, Profile, Business

class Profile_Form(forms.ModelForm):
    class meta:
        model = Profile
        fields = ('name', 'email')
    

class Business_Form(forms.ModelForm):
    class meta:
        model = Business
        fields = ('name', 'email')

class Jirani_Form(forms.ModelForm):
    class meta:
        model = Jirani
        fields = ('jirani_name', 'jirani_location', 'jirani_population')