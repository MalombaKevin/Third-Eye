from django import forms
from .models import Areacode, Profile_thirdeye, Business, User_Posts

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
        model = Areacode
        fields = ('area_name', 'area_location', 'area_population')
        exclude = ['user']

class Post_Form(forms.ModelForm):
    class Meta:
        model = User_Posts
        fields = ('category', 'content')
        exclude = ['user', 'profile']