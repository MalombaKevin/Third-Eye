from django.contrib import admin

from third_eye_app.models import Business, Profile, User_Posts

# Register your models here.
admin.site.register(Profile)
admin.site.register(Business)
admin.site.register(User_Posts)

