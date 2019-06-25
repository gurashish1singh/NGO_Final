from django.shortcuts import render, redirect
from .forms import UserProfileForm, UserForm, DonationForm
from .models import UserProfile, User
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
import datetime


def index_view(request, *args, **kwargs):
    return render(request, "index.html", {})

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
            print("user_obj.id = ", user_obj.id)
            print("user_obj.username = ", user_obj.username)
            print("user_obj type = ", type(user_obj))
            print("Saved main user, now saving the profile")
            up_obj = UserProfile.objects.get(user=user_obj)
            print("up_obj.user_profile.user.id = ", up_obj.user.id)
            print("up_obj.user_profile.user.username = ", up_obj.user.username)
            print("up_obj.id = ", up_obj.id)
            print("up_obj type = ", type(user_obj))
            print(userprofile_form['phone'].value())
            print(userprofile_form.data['phone'])
            up_obj.phone = userprofile_form['phone'].value()
            print("After user_obj Commit False ----")
            # up_obj_new.user = user_obj
            print("up_obj.user = ", up_obj.user.id)
            print("After setting the ForeignKey  ----")
            up_obj.save()
            print("After user_obj save ----")

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
            return HttpResponseRedirect('/login/')
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

