from django.shortcuts import render
from .models import UserProfile, EventList, Donations
from .forms import UserProfileForm, DonationForm
from django.http import HttpResponseRedirect
import datetime


def user_view(request):
    obj = UserProfile.objects.all()
    context = {
        'first_name': obj.first_name,
        'last_name': obj.last_name
    }
    return render(request, "donation_type.html", {context})


def user_profile_create_view(request):
    if request.method == 'POST':
        user_form = UserProfileForm(request.POST)
        print("user_profile_create_view:POST")
        if user_form.is_valid():
            user_form.save()
        return render(request, 'user_profile.html')
    else:
        print("user_profile_create_view:GET")
        user_form = UserProfileForm()
        return render(request, "userhome.html", {'form': user_form})


def donation_type_view(request):

    if request.method == 'POST':
        obj = EventList.objects.get(id)
        return render(request, "donation.html", {'event': obj})
    else:
        obj = EventList.objects.all()
        print("inside donation_type_view", request.method)
        print(obj)
        return render(request, "event_list.html", {'eventlist': obj})


def donation_amount_view(request):
    # print("Inside donation_amount_view")
    # print("Request Type in donation_amount_view:", request.method)
    # event_id = request.GET.get("event_id", "")
    # print("Got Request.data : ", event_id)
    # # Create a Donations object with the Event_id,
    # event_obj = EventList.objects.get(pk=event_id)
    # print("Got Event Object: ")
    # print(event_obj)
    # print("Event Name: ", event_obj.donation_type)
    # print("Event ID: ", event_obj.id)
    # donation_obj = Donations()
    # donation_obj.event_id = event_obj #EventList.objects.get(pk=event_id)
    # print("donation_obj.event_id = ", donation_obj.event_id)
    if request.method == 'POST':
        print("inside donation_view, after submitting input [ method = ]", request.method)
        donation_form = DonationForm(request.POST)
        print("Instantiated donation_form ...")
        donation_obj = donation_form.save(commit=False)
        print("Instantiated donation_model with event_id = ", donation_obj.event_id)
        print("Instantiated donation_model with donation_amount = ", donation_obj.donation_amount)
        print("Setting Values ...")
        username = None
        if request.user.is_authenticated:
            username = request.user.get_username()
        print("username = ", username)
        #print("Getting User object from this = ", UserProfile.objects.get())
        print("timestamp = ", datetime.datetime.now())
        donation_obj.timestamp = datetime.datetime.now()
        print("donation_obj.timestamp = ", donation_obj.timestamp)
        return HttpResponseRedirect("/login/")
    else:
        print("inside donation_view, before input method = ", request.method)
        donation_form = DonationForm()
        return render(request, "donation.html", {'donation_form': donation_form})


        return render(request, "event_list.html", {'eventlist': obj})


