from django.urls import path
from userapp.views import home_view
from .views import event_view, user_management_view, adduser_view, modifyuser_view, history_view

urlpatterns = [
    # path('', UserCreate.as_view()),
    path('home/', home_view),
    path('eventmanagement/', event_view),
    path('usermanagement/', user_management_view),
    path('adduser/', adduser_view),
    path('modifyuser/<int:user_id>', modifyuser_view),
    path('history/', history_view)

]
