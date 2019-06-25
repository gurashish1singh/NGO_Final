from django import forms
from .models import UserProfile, Donation
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'is_superuser')


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['phone']


        # 'CMA', 'phone','email', 'addr1', 'addr2', 'city', 'state','zipcode', 'country', 'urbanization']


class DonationForm(forms.ModelForm):
    class Meta:
        model = Donation
        fields = ['event', 'amount']

