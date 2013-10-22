from django import forms
from registration.forms import RegistrationForm
from .models import UserProfile
from localflavor.us.forms import USStateField, USStateSelect
from localflavor.us.us_states import US_STATES # , STATE_CHOICES, USPS_CHOICES
from PIL import Image as PImage
from os.path import join as pjoin
from django.contrib.auth.decorators import login_required


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ("user", "verified", "preferred_email")

        GENDER_CHOICES = (
            ('M', 'male'),
            ('F', 'female'),
            ('N', 'prefer not to specify')
        )
        gender = forms.ChoiceField(widget=forms.RadioSelect, choices=GENDER_CHOICES)
        state = forms.ChoiceField(required=True, widget = USStateSelect(), choices=US_STATES)


    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        self.fields['firstName'].label = "First Name"
        self.fields['middleName'].label = "Middle Name"
        self.fields['lastName'].label = "Last Name"
        self.fields['avatar'].label = "Profile Picture"


class RegistrationForm(RegistrationForm):
    # edu_email = forms.EmailField(required=True, label='FSU Email Address', max_length=75,
    #     help_text='Must end in @my.fsu.edu')

    model = UserProfile
    exclude = ("user", "verified", "preferred_email")

    firstName = forms.CharField(required=True, label="First Name")
    middleName = forms.CharField(required=False, label="Middle Name")
    lastName = forms.CharField(required=True, label="Last Name")
    bio = forms.CharField(widget = forms.Textarea)
    city = forms.CharField(required=True)
    state = forms.ChoiceField(required=True, widget = USStateSelect(), choices=US_STATES)
    avatar = forms.ImageField(required=False, label="Profile Image")
    

    GENDER_CHOICES = (
        ('N', 'prefer not to specify'),
        ('M', 'male'),
        ('F', 'female'),
    )

    gender = forms.ChoiceField(required=True, choices=GENDER_CHOICES)

