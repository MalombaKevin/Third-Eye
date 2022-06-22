from django.contrib import admin

from third_eye_app.models import Areacode, Business, Profile_thirdeye, User_Posts

# Register your models here.
admin.site.register(Profile_thirdeye)
admin.site.register(Business)
admin.site.register(User_Posts)
admin.site.register(Areacode)

