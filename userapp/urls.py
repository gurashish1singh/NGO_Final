from django.urls import path
from .views import user_profile_view , signup_view, home_view
from .views import donation_view

urlpatterns = [
    path('user_profile/', user_profile_view),
    path('signup/', signup_view),
    path('home/', home_view),
    path('donation/', donation_view)

]