from django import forms
from .models import Jirani, Profile_thirdeye, Business

class Add_Profile_Form(forms.ModelForm):
    class Meta:
        model = Profile_thirdeye
        fields = ('name', 'email', 'bio', 'profile_picture', 'phone_number')
        exclude = ['user']
    

class Business_Form(forms.ModelForm):
    class Meta:
        model = Business
        fields = ('name', 'email')
        exclude = ['user', 'profile']

class Jirani_Form(forms.ModelForm):
    class Meta:
        model = Jirani
        fields = ('jirani_name', 'jirani_location', 'jirani_population')
        exclude = ['user']