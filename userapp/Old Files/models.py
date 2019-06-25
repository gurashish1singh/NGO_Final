from django.db import models


class UserProfile(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    CMA = models.IntegerField()
    phone = models.CharField(max_length=50)
    email = models.EmailField()
    addr1 = models.CharField(max_length=50)
    addr2 = models.CharField(max_length=50)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    zipcode = models.CharField(max_length=20)
    country = models.CharField(max_length=20)
    urbanization = models.CharField(max_length=20)

    def __str__(self):
        return self.first_name, self.last_name


class EventList(models.Model):
    donation_type = models.CharField(max_length=50)

    def __str__(self):
        return self.donation_type


class Donations(models.Model):
    donation_type = models.CharField(max_length=50)
    userProfile_id = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    event_id = models.ForeignKey(EventList, on_delete=models.CASCADE)
    donation_amount = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField()

    def __str__(self):
        prt_string = "Donation_amount = " + self.donation_amount
        #prt_string = prt_string + "\n" + "UserProfile_id = " + UserProfile_id


