from django.shortcuts import render, redirect
from .forms import UserProfileForm, DonationForm, UserForm
from .models import UserProfile
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
import datetime

def index_view(request, *args, **kwargs):
    return render(request, "index.html", {})


def home_view(request, *args, **kwargs):
    print("inside Home_view ---- ")
    if request.user.is_authenticated:
        print("user is authenticated and finding type of request.user", request.user)
        user_obj = User.objects.get(username = request.user)
        print("got user Object :", user_obj.is_superuser)
        if user_obj.is_superuser:
            return render(request, "adminhome.html", {})
        else:
            return render(request, "userhome.html", {})

        # return HttpResponseRedirect(request, '//')
    else:
        return render(request, "home.html", {})


def signup_view(request):
    if request.method == 'POST':
        print("In signup_view, [Method = POST]")
        form = UserCreationForm(request.POST)
        userprofile_form = UserProfileForm(request.POST)
        print("User Form: ",form.is_valid())
        print("User Profile Form: ", userprofile_form.is_valid())
        if form.is_valid()and userprofile_form.is_valid():
            print("forms are valid, trying to save")
            user_obj = form.save()
            up_obj = UserProfile.objects.get(user=user_obj)

            up_obj.phone = userprofile_form['phone'].value()
            up_obj.save()
            print("user forms are saved")
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            print("Redirecting to /userapp/donation/...")
            return HttpResponseRedirect('/userapp/donation/')
    else:
        form = UserCreationForm()
        userprofile_form = UserProfileForm()
    return render(request, 'signup.html', {'form': form, 'userprofile_form': userprofile_form})


def user_profile_view(request):
    if request.method == 'POST':
        print("In user_profile_view, [Method = POST]")
        user_form = UserForm(request.POST, instance=request.user)
        userprofile_form = UserProfileForm(request.POST, instance=request.user.userprofile)
        print("user_form is populated")
        if user_form.is_valid() and userprofile_form.is_valid():
            print("forms are valid, trying to save")
            user_form.save()
            userprofile_form.save()
            print("user forms are saved")
            return HttpResponseRedirect('/home/')
        else:
            print("Form is not valid")
    else:
        print('In user_profile_view method = GET')
        user_form = UserForm(instance=request.user)
        print('After instantiating user_form ...')
        user_profile_form = UserProfileForm(instance=request.user.userprofile)
        print('After instantiating user_profile ...')
        return render(request, 'user_profile.html', {'user_form': user_form, 'user_profile_form': user_profile_form})


def donation_view(request):
    if request.method == 'POST':
        print("In donation_view, [Method = POST]")
        donation_form = DonationForm(request.POST)
        print("donation_form is populated")
        if donation_form.is_valid():
            print("donation form is valid, trying to save")
            donation_obj = donation_form.save(commit=False)
            print("Got donation_obj partially complete")
            donation_obj.user = request.user
            donation_obj.timestamp = datetime.datetime.now()
            print("Donation User = ", donation_obj.user.get_username())
            print("Donation Timestamp = ", donation_obj.timestamp)
            donation_obj.save()
            print("donation form is saved")
            return HttpResponseRedirect('/login/')
        else:
            print("Form is not valid")
    else:
        print('In user_profile_view method = GET')
        donation_form = DonationForm()
        print('After instantiating donation_form ...')
        return render(request, 'donation.html', {'donation_form': donation_form})


