from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#Profile class
class Profile_thirdeye(models.Model):
    name = models.CharField(max_length=100, null= True)
    email = models.EmailField(max_length=100, null=True)
    user= models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    bio= models.TextField(max_length=1000, null=True)
    profile_picture=models.ImageField(upload_to='images/', null=True)
    phone_number=models.CharField(max_length=10, blank=True, null=True)
    
    

    def __str__(self):
        return self.name
    
    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()
#Business class
class Business(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    profile = models.ForeignKey(Profile_thirdeye, on_delete=models.CASCADE, null = True, blank=True)
    user= models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name
    
    def save_business(self):
        self.save()
    
    def delete_business(self):
        self.delete()
#Posts class
class User_Posts(models.Model):
    category = models.CharField(max_length=200)
    content= models.CharField(max_length=200)
    profile = models.ForeignKey(Profile_thirdeye, on_delete=models.CASCADE, null = True, blank=True)
    user= models.ForeignKey(User, on_delete=models.CASCADE, null=True)

#Neighborhood class
class Jirani(models.Model):
    jirani_name = models.CharField(max_length=200)
    jirani_location= models.CharField(max_length=200)
    jirani_population =models.CharField(max_length=100)
    