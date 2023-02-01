from django.urls import path
from .views import createOrJoinRoom, create_token, getintoRoom, getMember

urlpatterns = [
    path('', createOrJoinRoom, name='roomCreate'),
    path('room/', getintoRoom, name='gotoRoom'),
    path('createToken/', create_token, name='createToken'),
    path('get_member/', getMember, name='getmember'),
]
