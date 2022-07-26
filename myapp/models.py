from cProfile import Profile
from django.db import models

# Create your models here.


class Newuser(models.Model):
    UserType = models.CharField(max_length=30)
    First_Name = models.CharField(max_length=30)
    Last_Name = models.CharField(max_length=100)
    image = models.ImageField(
        upload_to='profile_imgs', verbose_name='My Photo')
    Username = models.CharField(max_length=110)
    Email_Id = models.CharField(max_length=80)
    Password = models.CharField(max_length=30)
    Confirm_Password = models.CharField(max_length=30)
    Adress = models.CharField(max_length=300, default="NA")

    def __str__(self):
        return self.First_Name
