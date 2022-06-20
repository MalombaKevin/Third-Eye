from tkinter import CASCADE
from django.db import models

# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)

    def __str__(self):
        return self.name
    
    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

class Business(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null = True, blank=True)

    def __str__(self):
        return self.name
    
    def save_business(self):
        self.save()
    
    def delete_business(self):
        self.delete()