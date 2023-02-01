from django.urls import path
from .views import createOrJoinRoom, getintoRoom, get_token

urlpatterns = [
    path('', createOrJoinRoom, name='roomCreate'),
    path('room/', getintoRoom, name='gotoRoom'),
    path('getToken/', get_token, name='getToken'),
]
