from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser, AbstractBaseUser
# Create your models here.
class questions_model(models.Model):

    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name='questions')
    question = models.TextField()
    date=models.DateTimeField(default=timezone.now)
    #category_slug = models.CharField(max_length=200, default=1)



    def __str__(self):
        return self.question

class answers_model(models.Model):
    date=models.DateTimeField(default=timezone.now)
    answer = models.TextField(default='  ')
    question = models.ForeignKey(questions_model, default=1,  on_delete=models.CASCADE,related_name='answers')
    #series_summary = models.CharField(max_length=200)



    def __str__(self):
        return self.answer

class profile(models.Model):
    user = models.OneToOneField(User, default=1,on_delete=models.CASCADE)
    #  bio email college  profession

    bio=models.CharField(max_length = 190,default='None')
    email=models.CharField(max_length = 26,default='None')
    college=models.CharField(max_length = 50,default='None')
    profession=models.TextField(default='None')

    def __str__(self):
        return self.email
