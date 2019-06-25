from django import forms
from .models import UserProfile, Donations
from adminapp.models import User


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'CMA', 'phone','email', 'addr1', 'addr2', 'city', 'state','zipcode', 'country', 'urbanization']


class DonationForm(forms.ModelForm):
    class Meta:
        model = Donations
        fields = ['event_id', 'donation_amount']
#       donation_type = models.CharField(max_length=50)
# #     userProfile_id = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
# #     event_id = models.ForeignKey(EventList, on_delete=models.CASCADE)
# #     donation_amount = models.DecimalField(max_digits=10, decimal_places=2)
# #     timestamp = models.DateTimeField()