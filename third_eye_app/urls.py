from django.conf import settings
from django.urls import path
from django import views
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('profile/', views.profile, name='profile'),
    path('addProfile/', views.add_profile, name='addProfile'),
    path('addBusiness/', views.add_biashara, name='addBusiness'),
    path('addPosts/', views.add_post, name='addPost')

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)