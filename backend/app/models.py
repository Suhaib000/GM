from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django import forms
from django.contrib.auth.models import User, AbstractUser

# class My_User(AbstractUser):

# class UserTable(models.Model):
#     username = models.CharField(max_length=50, unique=True)
#     password = models.CharField(max_length=50)
#     usertype = models.CharField(max_length=50)



class PostJob(models.Model):
    jop_name = models.CharField(max_length=100)
    jop_discription = models.CharField(max_length=255)
    student_skills = models.CharField(max_length=255) 
    job_type =  models.CharField(max_length=255) 
    job_pay_type = models.CharField(max_length=255) 
    user  = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class AppliedJob(models.Model):
    user  = models.ForeignKey(User, on_delete=models.CASCADE)
    student_username = models.CharField(max_length=255) 
    job = models.ForeignKey(PostJob,on_delete=models.CASCADE)
    proposal =  models.TextField(max_length=4000)
    created_at = models.DateTimeField(auto_now_add=True)
    


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    usertype = models.CharField(max_length=50)
    about_you =  models.TextField(max_length=4000)



class Ranking(models.Model):
    user = models.ManyToManyField(User)
    rank =  models.IntegerField(validators=[MaxValueValidator(5),MinValueValidator(1)])
    
