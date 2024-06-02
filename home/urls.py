from django.contrib import admin
from django.urls import path,include
from home import views

urlpatterns = [
    
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('about', views.about, name='about'),
    path('project', views.project, name='project'),
    path('contact', views.contact, name='contact'),
    path('download/<int:file_id>/',views.download_file,name='download_file'),
]