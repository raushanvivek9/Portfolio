
# Create your models here.H
from distutils.command import upload
from pyexpat import model
from django.db import models


# class education(models.Model):
#     edu_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=30)
class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField() 
    phone = models.CharField(max_length=10)
    desc=models.TextField()
class Skill(models.Model):
    skill_name=models.CharField(max_length=30)
    skill_per=models.CharField(max_length=2)
class Education(models.Model):
    edu_name=models.TextField()
    edu_type=models.TextField()
    edu_unvi=models.TextField()
    edu_yr=models.CharField(max_length=4)
    edu_per=models.CharField(max_length=5)
class Project(models.Model):
    pro_name=models.CharField(max_length=30)
    pro_dis=models.TextField(max_length=230)
    pro_link=models.TextField()
    pro_tech=models.TextField()
    pro_type=models.CharField(max_length=30)
class Experince(models.Model):
    role_name=models.CharField(max_length=30)
    comp_name=models.CharField(max_length=30)
    skill_name=models.TextField()
    about_role=models.TextField(max_length=230)
    date_To=models.DateField()
    date_From=models.DateField()
class About(models.Model):
    about=models.TextField(max_length=1000)
    cv=models.FileField(upload_to='upload/')


