from django.db import models


# Create your models here.
class UserBase(models.Model):
    email = models.CharField('Email', max_length=50)
    nickname = models.CharField('Nickname', max_length=50)
    password = models.CharField('Password', max_length=100)

    def __str__(self):
        return self.email
    
