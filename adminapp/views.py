from django.shortcuts import render
from userapp.forms import DonationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .forms import EventForm
from userapp.forms import UserForm, UserProfileForm
from userapp.models import Event, UserProfile, Donation
from django.core.mail import send_mail
from django.http import HttpResponseRedirect,HttpResponse


# Create your views here.
# class UserCreate(ListView):
#     template_name = 'ngo/userhome.html'
#     queryset = User.objects.all()


def event_view(request):
    event_obj = Event.objects.all()
    print("Event obj", event_obj)
    if request.method == 'POST':
        print("In event_view, [Method = POST]")
        event_form = EventForm(request.POST)
        print("event Form: ", event_form.is_valid())
        if event_form.is_valid():
            print("forms are valid, trying to save")
            event_obj = event_form.save()
            print("event form is saved")
            print("Redirecting to /adminapp/eventmanagement/...")
            return HttpResponseRedirect('/adminapp/eventmanagement/')
    else:
        event_form = EventForm()
        print("In event_view, [Method = GET]")
        return render(request, 'addevent.html', {'event_form': event_form, 'event_obj': event_obj})


def user_management_view(request):
    user_obj = UserProfile.objects.all()
    print("In user_management_view, [Method = GET]")
    return render(request, 'user_view.html', {'user_obj': user_obj})

def history_view(request):
    donation_obj = Donation.objects.all()
    print("In history_view, [Method = GET]", donation_obj)
    return render(request, 'donation_view.html', {'donation_obj': donation_obj})


def adduser_view(request):
    if request.method == 'POST':
        print("In adduser_view, [Method = POST]")
        user_form = UserCreationForm(request.POST)
        print("User Form: ", user_form.is_valid())
        if user_form.is_valid():
            print("user forms is valid, trying to save")
            user_obj = user_form.save()
            print("user forms are saved, user_obj type = ", type(user_obj))
            username = user_form.cleaned_data.get('username')
            raw_password = user_form.cleaned_data.get('password1')
            redirect_url = "/adminapp/modifyuser/" + str(user_obj.id)
            print("Redirecting to ", redirect_url)
            return HttpResponseRedirect(redirect_url)
            # path('modifyuser/<int:user_id>', modifyuser_view),
        else:
            print("Form is not valid ---")
    else:
        form = UserCreationForm()
        return render(request, 'adduser.html', {'form': form})


def modifyuser_view(request, user_id):

    print("In Modifyuser_view, method = ", request.method)
    print("user_id =", user_id)
    if request.method == 'POST':
        print("In modifyuser_view, [Method = POST]")
        user_form = UserForm(request.POST)
        userprofile_form = UserProfileForm(request.POST)
        print("User Form: ", user_form.is_valid())
        print("User Profile Form: ", userprofile_form.is_valid())
        if user_form.is_valid():
            user_obj = user_form.save(commit=False)
            print("(before) user_obj.id = ", user_obj.id)
            user_obj.id = user_id
            print("(after) user_obj.id = ", user_obj.id)
            print("user_obj.username = ", user_obj.username)
            print("user_obj.first_name = ", user_obj.first_name)
            user_obj.save()
            print("saved user")
            print("Redirecting to /adminapp/usermanagement/...")
            return HttpResponseRedirect('/adminapp/usermanagement/')
        else:
            print("user_form is invalid")
        # if userprofile_form.is_valid():
        #     userprofile_form.save()
        #     print("Redirecting to /adminapp/usermanagement/...")
        #     return HttpResponseRedirect('/adminapp/usermanagement/')
        # else:
        #     print("userprofile_form is invalid")
    else:
        print("Instantiating the User with selected_user from before user_id= ", user_id)
        mod_user = User.objects.get(pk=user_id)
        print("mod_user.username = ", mod_user.username)
        user_form = UserForm(instance=mod_user)
        mod_up = UserProfile.objects.get(user=mod_user)
        print("mod_up.user.username = ", mod_up.user.username)
        userprofile_form = UserProfileForm(instance=mod_up)
        print("userprofile_form =", userprofile_form)
        print("Rendering it now: ")
    return render(request, 'usermodify.html', {'user_form': user_form, 'userprofile_form': userprofile_form})

    # {{ user_form.as_p}}
    # {{ userprofile_form.as_p}}

def modifyuser_view_new(request, user_id):

    print("In Modifyuser_view, method = ", request.method)
    print("user_id =", user_id)
    if request.method == 'POST':
        print("In modifyuser_view, [Method = POST]")
        user_form = UserForm(request.POST)
        userprofile_form = UserProfileForm(request.POST)
        print("userprofile_form.is_bound = ", userprofile_form.is_bound)
        print("userprofile_form.is_valid = ", userprofile_form.is_valid())
        print("User Form: ", user_form.is_valid())
        if user_form.is_valid() and user_form.is_valid():
            user_form_obj = user_form.save(commit=False)
            user_db_obj = User.objects.get(pk=user_id)
            user_db_obj.first_name = user_form_obj.first_name
            user_db_obj.last_name  = user_form_obj.last_name
            user_db_obj.email = user_form_obj.email

            print("user_db_obj.id = ", user_db_obj.id)
            print("user_db_obj.username = ", user_db_obj.username)
            print("user_db_obj.first_name = ", user_db_obj.first_name)
            user_db_obj.save()
            print("saved user")
            print("Now saving user_profile")
            up_db_obj = UserProfile.objects.get(user=user_db_obj)
            up_form_obj = userprofile_form.save(commit=False)
            up_db_obj.phone = up_form_obj.phone
            up_db_obj.save()
            print("Redirecting to /adminapp/usermanagement/...")
            return HttpResponseRedirect('/adminapp/usermanagement/')
        else:
            print("user_form is invalid")

    else:
        print("Instantiating the User with selected_user from before user_id= ", user_id)
        mod_user = User.objects.get(pk=user_id)
        print("mod_user.username = ", mod_user.username)
        user_form = UserForm(instance=mod_user)
        mod_up = UserProfile.objects.get(user=mod_user)
        print("mod_up.user.username = ", mod_up.user.username)
        userprofile_form = UserProfileForm(instance=mod_up)
        print("userprofile_form =", userprofile_form)
        print("userprofile_form.is_bound = ", userprofile_form.is_bound)
        print("userprofile_form.is_valid = ", userprofile_form.is_valid())
        print("Rendering it now: ")
    return render(request, 'usermodify.html', {'user_form': user_form, 'userprofile_form': userprofile_form})



def send_email(request):
    if request.method == "POST":
        email = request.POST["message"]
        send_mail('User.email',message,settings.EMAIL_HOST_USER,[sdingari@hotmail.com],fail_silently=False)
        return HttpResponse("Handling Post " + email)
    return render(request, 'send_email.html')