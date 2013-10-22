from django.db import models
from django.contrib.auth.models import User
from django.db.models import Count
from registration.signals import user_registered
from localflavor.us.forms import USStateField
from localflavor.us.us_states import US_STATES
import datetime


class UserProfile(models.Model):
    user = models.OneToOneField(User, unique=True)
    
    # Extra attributes
    firstName = models.CharField(max_length=40)
    middleName = models.CharField(max_length=40)
    lastName = models.CharField(max_length=40)
    bio = models.TextField(null=True)
    edu_email = models.EmailField(default='', max_length=254)
    preferred_email = models.EmailField(default='', max_length=254)
    verified = models.BooleanField(default=False)
    city = models.CharField(max_length=40)
    state = models.CharField(default='', max_length=20, choices=US_STATES)

    avatar = models.ImageField(upload_to='images/%Y/%m/%d',blank=True, null=True)


    GENDER_CHOICES = (
        ('M', 'male'),
        ('F', 'female'),
        ('N', 'prefer not to specify')
    )
    gender = models.CharField(default='N', max_length=2, choices=GENDER_CHOICES)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['username', 'firstName', 'lastName', 'edu_email', 'verified']

    def __unicode__(self):
        return "%s's profile" % self.user

# def create_profile(sender, instance, created, **kwargs):
#     if created:
#         profile, created = UserProfile.objects.get_or_create(user=instance)

# from django.db.models.signals import post_save
# post_save.connect(create_profile, sender=User)


def user_registered_callback(sender, user, request, **kwargs):
    profile = UserProfile(user = user)
    profile.firstName = request.POST["firstName"]
    profile.middleName = request.POST["middleName"]
    profile.lastName = request.POST["lastName"]
    profile.bio = request.POST["bio"]
    profile.gender = request.POST["gender"]
    profile.city = request.POST["city"]
    profile.state = request.POST["state"]
    # profile.avatar = request.POST["avatar"]

    profile.save()

 
user_registered.connect(user_registered_callback)

