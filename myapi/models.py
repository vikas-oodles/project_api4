from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Address(models.Model):
    street_address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pinCode = models.PositiveIntegerField()
    country = models.CharField(max_length=50)

    def __str__(self):
        return self.city

class Profile(AbstractUser):
    male = 'Male'
    female = 'Female'
    others = 'Others'

    choices = (
        (male, 'male'),
        (female,'female'),
        (others,'others')
    )

    phone_number = models.PositiveIntegerField()
    gender = models.CharField(choices=choices, max_length=10, default='Male',blank=True)
    profile_pic = models.ImageField(verbose_name='profile_pic',upload_to='profile_pics',blank=True)
    date_of_birth = models.DateTimeField(blank=True, verbose_name='DOB')
    address = models.OneToOneField(Address,related_name='profiles',on_delete=models.CASCADE)
    friends = models.ManyToManyField('self',symmetrical=False, blank=True)

    def __str__(self):
        return self.username