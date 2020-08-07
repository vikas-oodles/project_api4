from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

from .managers import ProfileManager
# Create your models here.

class Address(models.Model):
    street_address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pinCode = models.PositiveIntegerField()
    country = models.CharField(max_length=50)

    def __str__(self):
        return self.city

class Profile(AbstractBaseUser, PermissionsMixin):
    male = 'Male'
    female = 'Female'
    others = 'Others'

    choices = (
        (male, 'male'),
        (female,'female'),
        (others,'others')
    )
    email = models.EmailField(_('email_address'),unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    name = models.CharField(max_length=100, blank=False)
    phone_number = models.PositiveIntegerField(blank=False)
    gender = models.CharField(choices=choices, max_length=10, default='Male',blank=True, null=True)
    profile_pic = models.ImageField(verbose_name='profile_pic',upload_to='profile_pics',blank=True, null=True)
    date_of_birth = models.DateTimeField(blank=True, verbose_name='DOB', null=True)
    address = models.OneToOneField(Address,related_name='profiles',on_delete=models.CASCADE, blank=True, null=True)
    friends = models.ManyToManyField('self',symmetrical=False, blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone_number','name',]

    objects = ProfileManager()

    def __str__(self):
        return self.name