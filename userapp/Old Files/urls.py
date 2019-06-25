from django.contrib import admin
from django.urls import path

from .views import user_profile_create_view, donation_type_view, donation_amount_view

urlpatterns = [
    # path('', admin.site.urls),
    # path('donationtype/', donation_type_view),
    path('user_profile/', user_profile_create_view),
    path('event_list/', donation_type_view),
    path('donation_form/', donation_amount_view)

]